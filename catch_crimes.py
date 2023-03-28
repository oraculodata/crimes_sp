import asyncio
from playwright.async_api import Playwright, async_playwright
import config as cfg
import aux as func

path_write = 'files'

async def run(playwright: Playwright) -> None:
    try:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        page.set_default_timeout(timeout=0)

        await page.goto(cfg.ssp['portal'])
        await page.get_by_role("link", name=cfg.ssp['crime']).click()
        await page.get_by_role("link", name=cfg.ssp['ano']).click()
        await page.get_by_role("link", name=cfg.ssp['mes']).click()

        async with page.expect_download() as download_info:
            await page.locator(cfg.ssp['selector']).click()
        download = await download_info.value

        crime_name = func.fix_name(cfg.ssp['crime'])
        await download.save_as(path=f"{path_write}/{crime_name}_{cfg.ssp['mes'].lower()}_{cfg.ssp['ano']}.csv")

    except Exception as e:
        print(f"Erro: {e}")
        return
    finally:
        if 'browser' in locals():
            await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())

