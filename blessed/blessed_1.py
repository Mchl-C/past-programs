import blessed
term = blessed.Terminal()
print(term.height, term.width)

print(term.blink("Insert System disk into drive A:"))
print(term.underline_bold_green_on_yellow('They live! In sewers!'))
