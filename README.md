# calculator_python1
# 🧮 iPhone-Style Calculator

A sleek, modern calculator application built with Python's Tkinter, featuring an authentic iPhone calculator design with a dark theme and smooth interactions.


## ✨ Features

- **iPhone-Inspired Design**: Authentic iOS calculator aesthetic with circular buttons and color-coded operations
- **Dark Theme**: Pure black background with high-contrast buttons
- **Smooth Interactions**: Hover effects and visual feedback on all buttons
- **Mathematical Operations**: 
  - Basic operations: addition (+), subtraction (−), multiplication (×), division (÷)
  - Advanced functions: percentage (%), sign toggle (+/−)
  - Decimal support
- **Safe Expression Evaluation**: Uses Python's AST (Abstract Syntax Tree) for secure calculation
- **Error Handling**: Gracefully handles invalid expressions and mathematical errors

## 🎨 Design Highlights

- **Color Scheme**:
  - Numbers: Dark gray (#333333)
  - Operators: iPhone orange (#ff9f0a)
  - Functions: Light gray (#a5a5a5)
  - Background: Pure black (#000000)
- **Typography**: Helvetica Neue font family
- **Layout**: 4×5 grid matching iPhone calculator proportions
- **Responsive Buttons**: Hover states and smooth color transitions

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository or download the calculator file:
```bash
git clone https://github.com/yourusername/iphone-calculator.git
cd iphone-calculator
```

2. Run the calculator:
```bash
python calculator.py
```

### Usage

- **Numbers (0-9)**: Click to input numbers
- **Operators (+, −, ×, ÷)**: Click to add operations
- **AC**: Clear all input
- **+/−**: Toggle between positive and negative
- **%**: Convert current number to percentage
- **.**: Add decimal point
- **=**: Calculate the result

## 📝 Code Structure

```
calculator.py
├── Color Scheme Configuration
├── Button Creation Functions
│   ├── create_button()     # Creates styled buttons with hover effects
│   └── reset_operator_highlight()
├── Calculator Operations
│   ├── get_number()        # Handle number input
│   ├── get_operation()     # Handle operator input
│   ├── calculate()         # Evaluate expression using AST
│   ├── clear_all()         # Clear display
│   ├── toggle_sign()       # Change number sign
│   └── percentage()        # Convert to percentage
└── UI Layout
    ├── Display Frame       # Shows current input/result
    └── Button Grid         # 4×5 calculator button layout
```

## 🛡️ Security

This calculator uses Python's `ast.parse()` for safe expression evaluation, preventing code injection vulnerabilities that could occur with direct `eval()` usage.

## 🎯 Future Enhancements

- [ ] Scientific calculator mode with advanced functions (sin, cos, tan, log, etc.)
- [ ] Calculation history
- [ ] Keyboard input support
- [ ] Theme customization options
- [ ] Memory functions (M+, M-, MR, MC)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgments

- Design inspired by Apple's iOS Calculator app
- Built with Python's Tkinter library
- Uses AST for safe mathematical expression evaluation


---

**Note**: This is an educational project and is not affiliated with Apple Inc.
