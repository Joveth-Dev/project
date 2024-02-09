import pytest
from project import select_broomstick, fly_broomstick, get_random_broomstick


def test_select_broomstick(monkeypatch):
    # for valid input
    monkeypatch.setattr("builtins.input", lambda _: "1")
    selected_broomstick = select_broomstick()
    assert selected_broomstick["name"] == "Firebolt"

    monkeypatch.setattr("builtins.input", lambda _: "4")
    selected_broomstick = select_broomstick()
    assert selected_broomstick["name"] in [
        "Firebolt",
        "Nimbus 2000",
        "Cleansweep Seven",
    ]

    # for invalid input
    monkeypatch.setattr("builtins.input", lambda _: "invalid")
    with pytest.raises(SystemExit) as e:
        select_broomstick()
    assert e.value.code == "Enter a number from 1-4"


def test_fly_broomstick(monkeypatch, capsys):
    # for valid input 1
    monkeypatch.setattr("builtins.input", lambda _: "1")
    fly_broomstick("Soar through the skies like a blazing Firebolt!")
    captured = capsys.readouterr()
    assert "Soar through the skies like a blazing Firebolt!" in captured.out

    # for valid input 2
    monkeypatch.setattr("builtins.input", lambda _: "2")
    fly_broomstick("Any message")
    captured = capsys.readouterr()
    assert "Thanks for playing!" in captured.out

    # for invalid input
    monkeypatch.setattr("builtins.input", lambda _: "invalid")
    with pytest.raises(SystemExit) as e:
        fly_broomstick("Any message")
    assert e.value.code == "Enter either 1 or 2"


def test_get_random_broomstick():
    assert get_random_broomstick(1) == 1
    assert get_random_broomstick(3) in [1, 2, 3]
