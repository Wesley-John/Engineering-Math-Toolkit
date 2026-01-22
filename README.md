# ENGINEERING MATH TOOLKIT

## Table of Contents

- [Purpose](#purpose)
- [Tech Stack](#tech-stack)
- [Modules Overview](#modules-overview)
  - [Algebra](#algebra)
  - [Calculus](#calculus)
  - [Plotting](#plotting)
- [Numerical Differentiation (Central Difference)](#numerical-differentiation-central-difference)
- [Numerical Integration (Trapezoidal Rule)](#numerical-integration-trapezoidal-rule)
- [Why Numerical Methods Matter In Engineering](#why-numerical-methods-matter-in-engineering)
- [Limitations](#limitations)
- [Future Extensions](#future-extensions)

## Purpose

This project applies algebra and calculus concepts using numerical methods, reflecting how engineers solve problems in practice rather than symbolically.

The toolkit is designed to strengthen mathematical intuition, numeral thinking and software structure discipline for engineering applications.

## Tech Stack

- **Language** Python

## Modules Overview

### Algebra

- Solves linear equations of the form $ax + b = 0$
- Solves quadratic equations $ax^2 + bx + c = 0$
- Handles real and complex roots

### Calculus

- Numerical differentiation using the central difference method.
- Numeral integration using the trapezoidal rule.

### Plotting

- Visualizes mathematical functions over a given interval.

## Numerical Differentiation (Central Difference)

The derivative of a function is approximated as:

$$f'(x) = \frac{f(x + h) - f(x -h)}{2h}$$

This method is more accurate than forward differences because it reduces truncation error by considering the function behavior on both sides of the point.

The step size h must be chosen carefully:
- Too large → poor approximation
- Too small → floating-point

## Numerical Integration (Trapezoidal Rule)

The definite integral is approximated by dividing the interval into small sub-intervals and summing trapezoidal areas:

$$\int_{a}^{b} f(x) dx \approx h [\frac{f(a) + f(c)}{2} + \sum_{i=1}^{n-1} f(a + ih)]$$

This method is widely used in engineering to compute:
- Work
- Energy
- Signal Area
- Accumulated quantities

## Why Numerical Methods Matter in Engineering

Most real engineering systems:
- Cannot be solved symbolically
- Contain noise, nonlinearity, or discrete data

Numerical methods will allow engineers to approximate solutions reliably and are fundamental in:
- Control Systems
- Simulations
- Embedded Systems
- Signal Processing

## Limitations
- Accuracy depends on step size and number of intervals
- Discontinuous functions may give unreliable results
- No symbolic computation is used

## Future Extensions
- User-defined functions
- Error estimation
- Adaptive step sizing
- Application to physical systems

## Author

👤 **John Wesley**  

- [Connect with me on LinkedIn](https://www.linkedin.com/in/john-wesley-omondi)  
- [Connect with me on GitHub](https://github.com/Wesley-John)
