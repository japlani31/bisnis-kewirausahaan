"""
utils.py — BisnisKu PDF Generator
Shared utility untuk semua halaman di aplikasi BisnisKu.
"""
from fpdf import FPDF
import datetime


def _clean(text: str) -> str:
    """Sanitize string to Latin-1 (fpdf2 Helvetica safe)."""
    replacements = {
        "\u2014": "-", "\u2013": "-", "\u2012": "-",
        "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"',
        "\u2026": "...",
        "\u00d7": "x", "\u00f7": "/",
        "\u2264": "<=", "\u2265": ">=",
        "\u2248": "~", "\u00b1": "+/-",
        "\u03b2": "Beta", "\u03b1": "Alpha",
        "\u221e": "inf",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    # Drop any remaining non-Latin-1
    return text.encode("latin-1", errors="replace").decode("latin-1")


class BisnisKuPDF(FPDF):
    """PDF generator dengan header/footer branding BisnisKu."""

    BRAND    = "BisnisKu"
    INSTANSI = "Prodi S1 Kewirausahaan  |  FEB Universitas Muhammadiyah Metro"
    CREDIT   = "Koordinator: Ardiansyah Japlani, S.E., MBA"
    C_DARK   = (24,  50,  88)    # dark navy
    C_MID    = (80, 110, 150)    # medium blue-gray
    C_LIGHT  = (230, 240, 252)   # light blue fill
    C_GREEN  = (40, 130,  70)
    C_RED    = (170,  50,  50)
    C_AMBER  = (150, 100,  20)
    C_TEXT   = (55,  70,  90)

    def __init__(self, report_title: str = "Laporan Analisis Keuangan"):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.report_title = report_title
        self.set_auto_page_break(auto=True, margin=22)
        self.set_margins(14, 36, 14)

    # ── Header & Footer ──────────────────────────────────────────
    def header(self):
        r, g, b = self.C_DARK
        self.set_fill_color(r, g, b)
        self.rect(0, 0, 210, 32, "F")
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 16)
        self.set_xy(14, 5)
        self.cell(0, 8, self.BRAND)
        self.set_font("Helvetica", "", 9.5)
        self.set_xy(14, 14)
        self.cell(0, 5, _clean(self.report_title))
        self.set_font("Helvetica", "I", 7.5)
        self.set_xy(14, 20)
        self.cell(120, 4, self.INSTANSI)
        tgl = datetime.datetime.now().strftime("%d %B %Y  %H:%M")
        self.set_xy(14, 26)
        self.cell(0, 4, f"Dicetak: {tgl}", align="R")
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-13)
        r, g, b = self.C_MID
        self.set_draw_color(r, g, b)
        self.line(14, self.get_y(), 196, self.get_y())
        self.set_y(-11)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(120, 140, 165)
        self.cell(0, 4,
            f"{self.CREDIT}  |  BisnisKu · FEB UM Metro  |  Hal. {self.page_no()}",
            align="C")
        self.set_text_color(0, 0, 0)

    # ── Typography helpers ────────────────────────────────────────
    def section(self, title: str):
        self.ln(4)
        r, g, b = self.C_LIGHT
        self.set_fill_color(r, g, b)
        r2, g2, b2 = self.C_DARK
        self.set_draw_color(r2, g2, b2)
        self.set_text_color(r2, g2, b2)
        self.set_font("Helvetica", "B", 10.5)
        self.cell(0, 7, f"  {_clean(title)}", fill=True, ln=True, border="LB")
        self.set_text_color(0, 0, 0)
        self.set_draw_color(0, 0, 0)
        self.ln(2)

    def sub(self, title: str):
        self.set_font("Helvetica", "B", 9.5)
        r, g, b = self.C_DARK
        self.set_text_color(r, g, b)
        self.cell(0, 6, _clean(title), ln=True)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def kv(self, label: str, value: str, bold_val: bool = True):
        self.set_font("Helvetica", "", 9)
        r, g, b = self.C_MID
        self.set_text_color(r, g, b)
        self.cell(70, 5.5, f"  {_clean(label)}")
        self.set_font("Helvetica", "B" if bold_val else "", 9)
        r2, g2, b2 = self.C_TEXT
        self.set_text_color(r2, g2, b2)
        self.cell(0, 5.5, _clean(str(value)), ln=True)
        self.set_text_color(0, 0, 0)

    def note(self, text: str):
        self.set_font("Helvetica", "I", 7.5)
        r, g, b = self.C_MID
        self.set_text_color(r, g, b)
        self.multi_cell(0, 4.2, f"  Catatan: {_clean(text)}")
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def alert(self, text: str, ok: bool = True):
        if ok:
            self.set_fill_color(228, 248, 232)
            r, g, b = self.C_GREEN
        else:
            self.set_fill_color(252, 232, 232)
            r, g, b = self.C_RED
        self.set_draw_color(r, g, b)
        self.set_text_color(r, g, b)
        self.set_font("Helvetica", "B", 8.5)
        self.multi_cell(0, 5.5, f"  {_clean(text)}", fill=True, border="L")
        self.set_draw_color(0, 0, 0)
        self.set_text_color(0, 0, 0)
        self.ln(1)

    # ── Table helpers ─────────────────────────────────────────────
    def th(self, cols: list, widths: list, aligns: list | None = None):
        """Table header row."""
        if aligns is None:
            aligns = ["C"] * len(cols)
        r, g, b = self.C_DARK
        self.set_fill_color(r, g, b)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 8.5)
        for col, w, a in zip(cols, widths, aligns):
            self.cell(w, 6.5, _clean(str(col)), fill=True, align=a, border=0)
        self.ln()
        self.set_text_color(0, 0, 0)

    def tr(self, vals: list, widths: list, aligns: list | None = None,
           even: bool = False, bold: bool = False):
        """Table data row."""
        if aligns is None:
            aligns = ["L"] + ["C"] * (len(vals) - 1)
        bg = (242, 247, 253) if even else (255, 255, 255)
        self.set_fill_color(*bg)
        self.set_font("Helvetica", "B" if bold else "", 8.5)
        r, g, b = self.C_TEXT
        self.set_text_color(r, g, b)
        for val, w, a in zip(vals, widths, aligns):
            self.cell(w, 5.5, _clean(str(val)), fill=True, align=a, border="B")
        self.ln()
        self.set_text_color(0, 0, 0)

    # ── Build ─────────────────────────────────────────────────────
    def build(self) -> bytes:
        return bytes(self.output())
