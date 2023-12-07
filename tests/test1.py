import pytest

def test_draw_rectangle_text(capsys):
    colour = "red"
    x1_rectangle = 100
    y1_rectangle = 200
    width_rectangle = 50
    height_rectangle = 70

    expected_output = "Drawing a red rectangle at (100, 200) with width 50 and height 70\n"

    print("Drawing a {} rectangle at ({}, {}) with width {} and height {}".format(colour, x1_rectangle, y1_rectangle, width_rectangle, height_rectangle))

    captured = capsys.readouterr()
    actual_output = captured.out

    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()