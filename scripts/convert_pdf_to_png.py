"""将 assets 目录下的 PDF 文件转换为 PNG 图片"""

import subprocess
import sys
from pathlib import Path


def convert_pdf_to_png(assets_dir: str = "assets", dpi: int = 300):
    """使用 PyMuPDF (fitz) 将 PDF 转换为 PNG"""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("正在安装 PyMuPDF...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])
        import fitz

    assets_path = Path(assets_dir)
    pdf_files = list(assets_path.glob("*.pdf"))

    if not pdf_files:
        print("未找到 PDF 文件")
        return

    zoom = dpi / 72  # 72 is default PDF DPI
    matrix = fitz.Matrix(zoom, zoom)

    print(f"找到 {len(pdf_files)} 个 PDF 文件:")
    for pdf_file in pdf_files:
        png_path = pdf_file.with_suffix(".png")
        print(f"  转换: {pdf_file.name} -> {png_path.name}")
        try:
            doc = fitz.open(str(pdf_file))
            page = doc[0]  # 只取第一页
            pix = page.get_pixmap(matrix=matrix)
            pix.save(str(png_path))
            doc.close()
            print(f"    ✓ 完成")
        except Exception as e:
            print(f"    ✗ 转换失败: {e}")

    print("\n全部完成！")


if __name__ == "__main__":
    convert_pdf_to_png()
