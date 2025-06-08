# simple_load_string.py
"""
Load a blueprint from a string using simplex helpers.
"""

from draftsman.simplex import load

SAMPLE = "0eNqVlm9u4jAQhfc+inllr%2BCTMydnDBVg8drla6ZY2jYxO77Bh3qtQO%2FftzdvZzxU%2Fqnl5tpnWDNJpXWV1khzPEDBzwQ6k3oMNEmSYB9QZMmQbqUMzmgQBM%2Ftf%2FI3vp42jcZYabvtTtiSNj7FbJTwEoSYB4YprdbYK3XX1JO%2FsYlAfNGwzT67aRb%2FQuYkTQRShSXNBDOFgUaH%2F3reByJCcUTFo2K1YtpNcXoI5unQ4gfhwyy%2BVoKoyJIN6NIQtMVQOA%2FT%2BNqwZb%2FMoIcr2Y0NbUAlljAPVCGmaxc%2FuFcLJWpGfJU%2FXxdZLroPq%2BwRmjTLBOfxgjQGQUVvRBj%2FYnM0LbjcL52EBb9SP0ZwUZK9MP4CmuTnJj%2BkQEMhq9bKnTXVGrMz1USFza%2BhzqiFOUCAAlJca3yy%2Bj18%2FfsZotKtxptFhZptu0z9aUuw7F443bSyAyGVmRowb0Z%2BHP1n%2BD4f%2F9WXxJA6OsG9r3KtSA3p3pgtIHyG9eizvIZUl6KVC%2FKrwJpk%2BKy1ROVzpvjFnzJ4nLSfZpRMtGhP%2F9HwuSpzuWPXD%2Feo%2FfvXsYMB%2B%2F%2B1mZuqG6S035rn%2F4%2Fz6Xm9cV7u97t64Ovmtr0hg3ZdL5w%2F5B6vZDL%2FXRKl21Y8R%2FxPXe1cnb9ji7frQN%2Fs6Nm8qs6x%2Fvg4LEdBiC%2BWlg%2B9bbt7pudhp%2BJuSZ2pxxfOV0w%2FhufXoHLf6gpQ%3D"


def main() -> None:
    bp = load(SAMPLE)
    print(bp.label)


if __name__ == "__main__":
    main()
