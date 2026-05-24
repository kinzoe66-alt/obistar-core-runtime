import json

from runtime.review_exports.review_queue_exporter import (
    ReviewQueueExporter,
)


def test_exports_review_queue(tmp_path):
    export_path = (
        tmp_path /
        "review_queue.json"
    )

    routes = [
        {
            "candidate_id": "c1",
        }
    ]

    packages = [
        {
            "candidate_id": "c1",
        }
    ]

    result = (
        ReviewQueueExporter()
        .export(
            routes,
            packages,
            export_path,
        )
    )

    assert result["exported"] is True

    exported = json.loads(
        export_path.read_text()
    )

    assert exported["route_count"] == 1
    assert exported["package_count"] == 1
    assert exported["confirmed_issue"] is False


def test_handles_empty_exports(tmp_path):
    export_path = (
        tmp_path /
        "review_queue.json"
    )

    result = (
        ReviewQueueExporter()
        .export(
            [],
            [],
            export_path,
        )
    )

    exported = json.loads(
        export_path.read_text()
    )

    assert exported["route_count"] == 0
    assert exported["package_count"] == 0
