# Ai-for-siftware-week-1
# 🤖 CryptoBuddy - AI-Powered Cryptocurrency Advisor

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## 📋 Overview

**CryptoBuddy** is an intelligent, rule-based chatbot that helps users make informed cryptocurrency investment decisions by analyzing profitability and sustainability metrics. Built as part of Week 1 AI Course Assignment, this chatbot demonstrates fundamental AI decision-making logic.

## ✨ Features

- 💰 **Profitability Analysis**: Identifies trending cryptocurrencies with rising price trends
- 🌱 **Sustainability Scoring**: Recommends eco-friendly coins with low energy consumption
- 📊 **Comparative Analysis**: Side-by-side comparison of different cryptocurrencies
- 🎯 **Long-term Recommendations**: Balanced advice considering multiple factors
- ⚠️ **Risk Awareness**: Built-in disclaimers about crypto investment risks
- 💬 **Natural Conversation**: User-friendly interface with pattern matching

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/cryptobuddy.git
cd cryptobuddy
```

2. Run the chatbot:
```bash
python crypto_buddy.py
```

## 💡 Usage Examples

### Sample Conversations

```
You: Which crypto is most sustainable?
CryptoBuddy: 🌱 Most Sustainable: Cardano (ADA)
             Sustainability Score: 8/10
             This is great for long-term, eco-conscious investing! 🌍

You: Show me rising cryptocurrencies
CryptoBuddy: 📈 Rising Cryptocurrencies:
             🚀 Bitcoin (BTC) - Market Cap: High
             🚀 Cardano (ADA) - Market Cap: Medium
             🚀 Solana (SOL) - Market Cap: Medium

You: Compare Bitcoin and Cardano
CryptoBuddy: ⚖️  Comparing Bitcoin vs Cardano:
             [Detailed comparison table displayed]
```

### Available Commands

- `help` - Show example questions
- `list` or `list all` - Display all cryptocurrencies
- `quit` or `exit` - End conversation

### Query Types

1. **Sustainability Queries**: "What's the most sustainable coin?", "Show eco-friendly options"
2. **Trend Queries**: "Which crypto is rising?", "Show trending coins"
3. **Investment Advice**: "Best long-term investment?", "Where should I invest?"
4. **Comparisons**: "Compare Bitcoin and Ethereum"
5. **Details**: "Tell me about Cardano", "Info on Solana"
6. **Energy Efficiency**: "Which has low energy use?"

## 🗂️ Project Structure

```
cryptobuddy/
│
├── crypto_buddy.py          # Main chatbot code
├── README.md                # This file
├── screenshots/             # Screenshots folder
│   ├── conversation1.png
│   ├── conversation2.png
│   └── features.png
└── requirements.txt         # Dependencies (none required)
```

## 🧠 How It Works

### Decision-Making Logic

CryptoBuddy uses **rule-based AI** to make recommendations:

1. **Pattern Matching**: Analyzes user input for keywords (sustainable, rising, compare, etc.)
2. **Data Filtering**: Applies filters based on user intent
3. **Scoring Algorithm**: For long-term recommendations, calculates scores:
   - Rising trend: +3 points
   - High market cap: +2 points
   - Sustainability score: +0-10 points
4. **Response Generation**: Formats and presents data with appropriate emojis and explanations

### Cryptocurrency Database

Each cryptocurrency contains:
- **Symbol**: Ticker symbol (BTC, ETH, etc.)
- **Price Trend**: Rising/Stable/Falling
- **Market Cap**: High/Medium/Low
- **Energy Use**: High/Medium/Low
- **Sustainability Score**: 1-10 rating
- **Risk Level**: Investment risk assessment
- **Description**: Brief explanation of the cryptocurrency

## 📊 Current Database

| Cryptocurrency | Symbol | Trend | Sustainability | Energy Use |
|---------------|--------|-------|----------------|------------|
| Bitcoin       | BTC    | Rising| 3/10          | High       |
| Ethereum      | ETH    | Stable| 6/10          | Medium     |
| Cardano       | ADA    | Rising| 8/10          | Low        |
| Solana        | SOL    | Rising| 7/10          | Low        |
| Polkadot      | DOT    | Stable| 7/10          | Low        |

## 🎓 Learning Outcomes

Through this project, you'll understand:

✅ **AI Decision-Making**: How rule-based systems make recommendations  
✅ **Conversational Design**: Creating natural user interactions  
✅ **Data Analysis**: Processing and comparing structured data  
✅ **Pattern Matching**: Recognizing user intent from text  
✅ **Python Programming**: Classes, dictionaries, string manipulation

## 🔮 Future Enhancements (Stretch Goals)

- [ ] **API Integration**: Pull real-time data from CoinGecko API
- [ ] **NLP Processing**: Use NLTK for more natural language understanding
- [ ] **Historical Analysis**: Track price trends over time
- [ ] **Portfolio Management**: Help users manage multiple investments
- [ ] **Risk Calculator**: Personalized risk assessment
- [ ] **Web Interface**: Flask/Django web application
- [ ] **Database Storage**: PostgreSQL/MongoDB for data persistence

## ⚠️ Disclaimer

**Important**: This chatbot is for educational purposes only. Cryptocurrency investments carry significant risks. Always:
- Do your own research (DYOR)
- Consult with financial advisors
- Never invest more than you can afford to lose
- Understand the technology and projects before investing

## 📝 Assignment Reflection

### How does this chatbot mimic basic AI decision-making?

CryptoBuddy demonstrates AI decision-making through pattern recognition, data analysis, and rule-based logic. It processes natural language inputs, matches them against predefined patterns, filters cryptocurrency data based on multiple criteria, and generates personalized recommendations. The scoring system for long-term investments shows how AI weighs different factors to make optimal decisions—similar to how machine learning models evaluate features, but using explicit rules rather than learned patterns.

## 👨‍💻 Author

**Your Name**  
PLP Academy - Week 1 AI Assignment  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PLP Academy for the comprehensive AI curriculum
- CoinGecko for cryptocurrency data inspiration
- The crypto community for sustainability awareness

## 📞 Contact

Questions or suggestions? Feel free to reach out!
- GitHub Issues: [Create an issue](https://github.com/yourusername/cryptobuddy/issues)
- Email: your.email@example.com

---

**Made with 💚 for the PLP Academy AI Course**

*Remember: Stay curious, code boldly, and invest wisely!* 🚀
