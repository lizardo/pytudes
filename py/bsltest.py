from __future__ import print_function

################ Tests for bsl.py

bsl_tests = [
    # Values

    ## Numbers
    ('1', 1),
    ('3.5', 3.5),
    ('1/2', 0.5),
    ('#i1.4142135623730951', 1.4142135623730951),

    ## Strings
    ('"Marvolo"', 'Marvolo'),
    ## Images (TODO)

    ## Booleans
    ('true', True),
    ('false', False),

    ## Compound data
    ('(make-person "Claude" "Monet")', ('Claude', 'Monet')),

    ## Lists
    ('empty', []),
    ('(cons 2 (cons 1 empty))', [2, 1]),
    ('(cons "x" (cons "y" (cons "z" empty)))', ['x', 'y', 'z']),

    # Primitive Operations
    ('(+ 2 2)', 4),
    ('(- 2 1)', 1),
    ('(* 3 3)', 9),
    ('(/ 4 2)', 2),
    # TODO
    #string-append, string-length, substring ...
    #circle, square, overlay, above, beside...
    #not, =, <, >, string=?, string<?, cons, first, rest, empty?, cons?

    # Forming Definitions
    ('(define x 3)', None),
    ('x', 3),
    ('(+ x x)', 6),
    # TODO
    #(define (bulb c)              ;defines a function named bulb, with parameter c
    #  (circle 30 "solid" c))      ;this is the body of the function
    #(define-struct wand (wood core length))  ;defines the functions below:
    #; constructor: make-wand
    #; selectors:   wand-wood, wand-core, wand-length
    #; predicate:   wand?

    # Forming Expressions
    ('(+ (* 2 100) (* 1 10))', 210),
    ('(if (> 6 5) (+ 1 1) (+ 2 2))', 2),
    ('(if (< 6 5) (+ 1 1) (+ 2 2))', 4),
    ('(cond [(> x 4) "more"]\
            [(< x 4) "less"]\
            [else "same"])', 'less'),
    ('(and (< 0 x) (>= x 10))', False),
    ('(or (< x 0) (> x 10))', False),
]


def test(tests, name=''):
    "For each (exp, expected) test case, see if eval(parse(exp)) == expected."
    fails = 0
    for (x, expected) in tests:
        try:
            result = eval(parse(x))
            print(x, '=>', str(result))
            ok = (result == expected)
        except Exception as e:
            print(x, '=raises=>', type(e).__name__, e)
            ok = isinstance(expected, type) and \
                issubclass(expected, Exception) and isinstance(e, expected)
        if not ok:
            fails += 1
            print('FAIL!!!  Expected', expected)
    print('%s %s: %d out of %d tests fail.' %
          ('*' * 45, name, fails, len(tests)))


if __name__ == '__main__':
    from bsl import *
    test(bsl_tests, 'bsl.py')
