from project import get_mode, Solo, Vs
import pytest


def test_get_mode():
    with pytest.raises(Exception):
        get_mode("3")

    with pytest.raises(Exception):
        get_mode("cat")

def test_solo(monkeypatch):
   monkeypatch.setattr("builtins.input", lambda _: "2")
   i = int(input("Guess a number: "))
   assert i == 2

def test_vs(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")
    g = int(input("Guess a number: "))
    assert g == 3