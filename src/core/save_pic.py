from core.metadata_from_json import dztiles_url, artist_and_title
from core.format_url import image_json
from core.main import get_tiles_and_save
from core.loggers import save_pic_logger, high_alert_logger

MAX_DZNUM = 13


def amend_dz_url(root_url: str, dz_num) -> str:
    if not isinstance(dz_num, int) and not dz_num.isdigit():
        raise ValueError("dz_num must be an integer")
    stem = root_url.rsplit("/", 2)
    stem[-2] = str(dz_num)  # TODO Why???????
    return "/".join(stem)


def save_pic(artsy_url):
    bootstrap = image_json(artsy_url)
    jpeg_label = artist_and_title(bootstrap)
    root_url = dztiles_url(bootstrap)
    if root_url:
        save_pic_logger.info(f"attempting to fetch: {artsy_url} ...")
        save_pic_logger.info(f"artwork name: {jpeg_label}")
        dz_num_counter = MAX_DZNUM
        while dz_num_counter > 8:
            amended_dz_url = amend_dz_url(root_url, dz_num_counter)
            save_pic_logger.info(f"dztiles number was too large. Trying {dz_num_counter} as {amended_dz_url} ...")
            if get_tiles_and_save(amended_dz_url, jpeg_label):
                if dz_num_counter == MAX_DZNUM:
                    high_alert_logger.debug(f"picture bigger than MAX_DZNUM {MAX_DZNUM}!")
                save_pic_logger.info("successfully saved picture.")
                return(get_tiles_and_save(amended_dz_url, jpeg_label))  # return value is file path and title_artist
            dz_num_counter -= 1
    else:
        save_pic_logger.info(f"{jpeg_label} has no high resolution version. Skipping.")
        return("no high res version")


# put in a different file

if __name__ == '__main__':
    save_pic("https://www.artsy.net/artwork/jeremy-okai-davis-fix")  # vanilla dz 11
    # save_pic("https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern")  # jpg only, no dz
    # save_pic("https://www.artsy.net/artwork/dapper-bruce-lafitte-no-summercamp")   # dz 13
