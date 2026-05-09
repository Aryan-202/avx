import flet as ft

def main(page: ft.Page):
    page.title = "AVX UI"
    
    def handle_convert(e):
        # Call your existing conversion logic
        page.add(ft.Text(f"Result:"))
    
    page.add(
        ft.Text("AVX Converter", size=30),
        ft.ElevatedButton("Convert", on_click=handle_convert),
    )

ft.app(target=main)