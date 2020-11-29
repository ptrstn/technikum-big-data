from bigchina.data import read_all_unihan_files, read_all_hsk_files, download_unihan_zip


def test_download_unihan():
    download_unihan_zip()


def test_unihan_read():
    dataframe = read_all_unihan_files()
    assert len(list(dataframe)) == 3


def test_hsk_read():
    dataframe = read_all_hsk_files()
    assert len(list(dataframe)) == 2
