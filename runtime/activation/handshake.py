from runtime.contract_validator import validate_contract

class AuthorityHandshake:

    def __init__(self, runtime_surface: str):
        self.runtime_surface = runtime_surface

    def admit(self, authority_doc: dict):

        validate_contract(authority_doc)

        blocked = authority_doc.get("blocked_runtime_behavior", [])

        if self.runtime_surface in blocked:
            raise PermissionError(
                f"Surface '{self.runtime_surface}' blocked by authority"
            )

        return {
            "admitted": True,
            "surface": self.runtime_surface,
            "authority": authority_doc.get("name"),
            "version": authority_doc.get("version")
        }
