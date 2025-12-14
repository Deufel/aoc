# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "anthropic==0.75.0",
#     "beautifulsoup4==4.14.3",
#     "httpx==0.28.1",
#     "pytest==9.0.2",
#     "python-dotenv==1.2.1",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(
    width="columns",
    app_title="Advent of Code",
    auto_download=["html"],
)

with app.setup:
    import httpx, os, re, calendar
    from bs4 import BeautifulSoup
    from datetime import datetime, date
    from dotenv import load_dotenv


    load_dotenv() 
    SESSION = os.getenv("SESSION") or input("Paste SESSION cookie: ")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code: 2025
    > Mike Deufel
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pytest
    return (mo,)


@app.cell
def _():
    show_dec(one=[], two=[1, 2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Utils
    """)
    return


@app.function
def get_data(
    d=None,            # day
    y:None = 2025,     # year
) -> str:              # aoc data
    "request puzzel data"
    c={'session': SESSION}
    url=f"https://adventofcode.com/{y}/day/{d}/input"
    r = httpx.get(url, cookies=c)
    return r.text


@app.function
def show_dec(one=[], two=[]):
    calendar.setfirstweekday(6)
    print(f"    December 2025")
    print(" ".join(f" {day}" for day in calendar.day_abbr))
    for wk in calendar.monthcalendar(2025, 12):
        row = []
        for d in wk:
            if d == 0: row.append("    ")
            elif d in two: row.append(f"{d:2d}**")
            elif d in one: row.append(f"{d:2d}*_")
            else: row.append(f"{d:2d}__")
        print(" ".join(row))


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Solutions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1
    """)
    return


@app.cell
def _():
    def day1():
        # Get data
        data = get_data(d=1, y=2025)
        rots = [int(x) for x in data.replace("R","").replace("L","-").splitlines()]

        # Part 1: count landings on 0
        pos,cnt1 = 50,0
        for r in rots:
            pos += r
            if pos % 100 == 0: cnt1 += 1

        # Part 2: count passes through 0
        pos,cnt2 = 50,0
        for r in rots:
            for i in range(pos, pos+r, 1 if r>0 else -1):
                if i % 100 == 0: cnt2 += 1
            pos += r

        print(f"Day 1\n\t{cnt1=}\n\t{cnt2=}")

    day1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2
    """)
    return


@app.cell
def _():
    def divisors(n: int) -> list:
        """Returns all proper divisors of n (excluding n itself)."""
        return [i for i in range(1, n//2+1) if n%i==0]

    def is_repeating(s: str) -> bool:
        """Check if s is a pattern repeated at least twice."""
        n = len(s)
        for sz in divisors(n):
            if s[:sz]*(n//sz)==s: return True
        return False

    def day2():
        data = get_data(d=2, y=2025).strip()

        # Part 1: first half == second half
        tot1 = 0
        for rng in data.split(","):
            a,b = map(int, rng.split("-"))
            for i in range(a, b+1):
                s = str(i)
                if s[:len(s)//2]==s[len(s)//2:]: tot1 += i

        # Part 2: any repeating pattern
        tot2 = 0
        for rng in data.split(","):
            a,b = map(int, rng.split("-"))
            for i in range(a, b+1):
                if is_repeating(str(i)): tot2 += i

        print(f"Day 2\n\t{tot1=}\n\t{tot2=}")


    day2()
    return day2, divisors, is_repeating


@app.cell
def _(divisors, is_repeating):
    def test_divisors():
        assert divisors(5) == [1]
        assert divisors(16) == [1,2,4,8]
        assert divisors(43) == [1]

    def test_is_repeating():
        assert is_repeating("11") == True
        assert is_repeating("12") == False 
        assert is_repeating("103103104") == False 
        assert is_repeating("103103103") == True 
        assert is_repeating("1111111") == True
    return


@app.cell
def _(day2):
    day2()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3
    """)
    return


@app.cell
def _():
    d = get_data(3)
    print(f'''
        {type(d) = }
        {d[:20]  = }
        {d[-20:] = }
        {len(d)  = :,}
    ''')
    return (d,)


@app.cell
def _(d):
    print(d)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
