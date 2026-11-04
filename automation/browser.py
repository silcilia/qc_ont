
from playwright.sync_api import sync_playwright


def open_device_gui(ip_address):
    """
    Membuka GUI ONT dan mengambil informasi awal halaman.
    Tidak melakukan login atau mengubah konfigurasi perangkat.
    """

    url = f"http://{ip_address}"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:
            response = page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=15000
            )

            page.wait_for_timeout(2000)

            # Informasi dasar halaman
            title = page.title()
            current_url = page.url

            # Mengambil informasi elemen input
            inputs = page.locator("input").evaluate_all("""
                elements => elements.map(element => ({
                    type: element.type,
                    name: element.name,
                    id: element.id,
                    placeholder: element.placeholder
                }))
            """)

            # Mengambil informasi tombol
            buttons = page.locator(
                "button, input[type=submit]"
            ).evaluate_all("""
                elements => elements.map(element => ({
                    text: element.innerText,
                    value: element.value,
                    type: element.type
                }))
            """)

            # Mengambil teks halaman
            page_text = page.locator("body").inner_text(
                timeout=5000
            )

            # Simpan screenshot halaman untuk analisis
            page.screenshot(
                path="device_gui.png",
                full_page=True
            )

            result = {
                "ip_address": ip_address,
                "url": current_url,
                "http_status": (
                    response.status if response else None
                ),
                "title": title,
                "inputs": inputs,
                "buttons": buttons,
                "page_text": page_text[:3000],
            }

            return result

        except Exception as error:
            return {
                "ip_address": ip_address,
                "error": str(error)
            }

        finally:
            browser.close()
