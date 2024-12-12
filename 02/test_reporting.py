import golf
import reporting

def test_both_implementations():
    expected = {"part1": 564, "part2": 604}
    print(f"expected: {expected}")
    mark = reporting.process_reports()
    print(f"mark's version: {mark}")
    assert mark == expected
    golfed = golf.process_reports()
    print(f"claude's version: {golfed}")
    assert golfed == expected
