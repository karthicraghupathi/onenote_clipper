#!/usr/bin/env python

import argparse
import asyncio
from urllib.parse import urlparse

from pyppeteer import launch
from slugify import slugify

import settings
from settings import logger


async def html_to_png(url: str) -> None:
    browser = await launch(ignoreHTTPSErrors=True)
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot(
        path="{}.png".format(slugify(url)),
        fullPage=True,
        quality=100,
        omitBackground=True,
    )
    await browser.close()


def main(args):
    asyncio.get_event_loop().run_until_complete(html_to_png(args.url))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clip webpages to OneNote.")
    parser.add_argument(
        "url",
        type=str,
        help="The URL of the webpage to clip.",
    )
    args = parser.parse_args()

    logger.info("Running {}".format(settings.PROJECT_NAME))
    main(args)
