import runpy
import main


def test_main(capsys):
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"


def test_main_as_script(capsys):
    runpy.run_module("main", run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
