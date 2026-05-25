from companion_safety_eval.transcript import Transcript, TranscriptEvent


def test_transcript_round_trip(tmp_path):
    path = tmp_path / "transcript.jsonl"
    transcript = Transcript(path)
    event = TranscriptEvent(scenario_id="s1", turn_index=1, role="user", content="hello", metadata={"x": 1})
    transcript.append(event)
    loaded = Transcript.load(path)
    assert len(loaded) == 1
    assert loaded[0].content == "hello"
    assert loaded[0].metadata == {"x": 1}
