"""
CryptoBuddy - Your AI-Powered Cryptocurrency Advisor
A rule-based chatbot for cryptocurrency investment advice
"""

import re
from datetime import datetime

# Cryptocurrency Database
crypto_db = {
    "Bitcoin": {
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3,
        "risk_level": "medium",
        "description": "The original cryptocurrency and digital gold"
    },
    "Ethereum": {
        "symbol": "ETH",
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6,
        "risk_level": "medium",
        "description": "Smart contract platform with wide adoption"
    },
    "Cardano": {
        "symbol": "ADA",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "risk_level": "medium-high",
        "description": "Eco-friendly blockchain with research-driven approach"
    },
    "Solana": {
        "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "high",
        "description": "High-speed blockchain for DeFi and NFTs"
    },
    "Polkadot": {
        "symbol": "DOT",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "high",
        "description": "Multi-chain platform connecting blockchains"
    }
}

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.conversation_count = 0
        
    def greet(self):
        """Welcome message"""
        print(f"\n{'='*60}")
        print(f"🤖 Hey there! I'm {self.name}, your crypto sidekick! 🚀")
        print(f"{'='*60}")
        print("I can help you find cryptocurrencies based on:")
        print("  💰 Profitability (trending coins)")
        print("  🌱 Sustainability (eco-friendly options)")
        print("  📊 Market cap and stability")
        print("\nType 'help' for example questions or 'quit' to exit.")
        print(f"{'='*60}\n")
    
    def show_help(self):
        """Display help menu"""
        print("\n📚 Here are some questions you can ask me:")
        print("  • 'Which crypto is most sustainable?'")
        print("  • 'Show me rising cryptocurrencies'")
        print("  • 'What's the best long-term investment?'")
        print("  • 'Compare Bitcoin and Cardano'")
        print("  • 'List all cryptos'")
        print("  • 'Tell me about Ethereum'")
        print("  • 'Which has low energy use?'\n")
    
    def list_cryptos(self):
        """List all available cryptocurrencies"""
        print("\n📋 Available Cryptocurrencies:\n")
        for name, data in crypto_db.items():
            trend_emoji = "📈" if data["price_trend"] == "rising" else "📊"
            eco_emoji = "🌱" if data["sustainability_score"] >= 7 else "⚡"
            print(f"{trend_emoji} {eco_emoji} {name} ({data['symbol']})")
            print(f"   Price: {data['price_trend'].title()} | "
                  f"Sustainability: {data['sustainability_score']}/10")
        print()
    
    def get_crypto_details(self, crypto_name):
        """Show detailed information about a cryptocurrency"""
        crypto_name = crypto_name.title()
        if crypto_name in crypto_db:
            data = crypto_db[crypto_name]
            print(f"\n💎 {crypto_name} ({data['symbol']}) Details:")
            print(f"{'─'*50}")
            print(f"📝 {data['description']}")
            print(f"📈 Price Trend: {data['price_trend'].title()}")
            print(f"💰 Market Cap: {data['market_cap'].title()}")
            print(f"⚡ Energy Use: {data['energy_use'].title()}")
            print(f"🌱 Sustainability Score: {data['sustainability_score']}/10")
            print(f"⚠️  Risk Level: {data['risk_level'].title()}")
            print(f"{'─'*50}\n")
        else:
            print(f"\n❌ Sorry, I don't have data on {crypto_name} yet!\n")
    
    def recommend_sustainable(self):
        """Recommend most sustainable cryptocurrency"""
        best = max(crypto_db.items(), key=lambda x: x[1]["sustainability_score"])
        name, data = best
        print(f"\n🌱 Most Sustainable: {name} ({data['symbol']})")
        print(f"Sustainability Score: {data['sustainability_score']}/10")
        print(f"Energy Use: {data['energy_use'].title()}")
        print(f"💡 Why? {data['description']}")
        print(f"This is great for long-term, eco-conscious investing! 🌍\n")
    
    def recommend_profitable(self):
        """Recommend cryptocurrencies with rising trends"""
        rising = [(n, d) for n, d in crypto_db.items() if d["price_trend"] == "rising"]
        if rising:
            print("\n📈 Rising Cryptocurrencies:\n")
            for name, data in rising:
                print(f"🚀 {name} ({data['symbol']})")
                print(f"   Market Cap: {data['market_cap'].title()}")
                print(f"   Sustainability: {data['sustainability_score']}/10")
                print(f"   Risk: {data['risk_level'].title()}\n")
        else:
            print("\n📊 No cryptocurrencies are currently trending up.\n")
    
    def recommend_long_term(self):
        """Recommend best for long-term investment"""
        # Balance profitability and sustainability
        scored = []
        for name, data in crypto_db.items():
            score = 0
            if data["price_trend"] == "rising":
                score += 3
            if data["market_cap"] == "high":
                score += 2
            score += data["sustainability_score"]
            scored.append((name, data, score))
        
        best = max(scored, key=lambda x: x[2])
        name, data, score = best
        
        print(f"\n🎯 Best Long-Term Investment: {name} ({data['symbol']})")
        print(f"{'─'*50}")
        print(f"📊 Overall Score: {score}/15")
        print(f"📈 Trend: {data['price_trend'].title()}")
        print(f"🌱 Sustainability: {data['sustainability_score']}/10")
        print(f"💰 Market Cap: {data['market_cap'].title()}")
        print(f"\n💡 {data['description']}")
        print(f"{'─'*50}\n")
    
    def compare_cryptos(self, query):
        """Compare two cryptocurrencies"""
        # Extract crypto names from query
        cryptos_found = []
        for name in crypto_db.keys():
            if name.lower() in query.lower():
                cryptos_found.append(name)
        
        if len(cryptos_found) >= 2:
            crypto1, crypto2 = cryptos_found[0], cryptos_found[1]
            data1, data2 = crypto_db[crypto1], crypto_db[crypto2]
            
            print(f"\n⚖️  Comparing {crypto1} vs {crypto2}:\n")
            print(f"{'Metric':<25} {crypto1:<15} {crypto2:<15}")
            print(f"{'─'*55}")
            print(f"{'Price Trend':<25} {data1['price_trend']:<15} {data2['price_trend']:<15}")
            print(f"{'Market Cap':<25} {data1['market_cap']:<15} {data2['market_cap']:<15}")
            print(f"{'Energy Use':<25} {data1['energy_use']:<15} {data2['energy_use']:<15}")
            print(f"{'Sustainability Score':<25} {str(data1['sustainability_score'])+'/10':<15} {str(data2['sustainability_score'])+'/10':<15}")
            print(f"{'Risk Level':<25} {data1['risk_level']:<15} {data2['risk_level']:<15}")
            print(f"{'─'*55}\n")
        else:
            print("\n❌ Please mention two cryptocurrencies to compare!\n")
    
    def find_low_energy(self):
        """Find cryptocurrencies with low energy use"""
        low_energy = [(n, d) for n, d in crypto_db.items() if d["energy_use"] == "low"]
        if low_energy:
            print("\n⚡ Low Energy Cryptocurrencies:\n")
            for name, data in low_energy:
                print(f"🌱 {name} ({data['symbol']})")
                print(f"   Sustainability: {data['sustainability_score']}/10")
                print(f"   Trend: {data['price_trend'].title()}\n")
        else:
            print("\n❌ No low-energy cryptocurrencies found.\n")
    
    def process_query(self, query):
        """Process user query and provide appropriate response"""
        query = query.lower().strip()
        
        # Handle commands
        if query in ['quit', 'exit', 'bye']:
            return False
        
        if query == 'help':
            self.show_help()
            return True
        
        if query in ['list', 'list all', 'show all', 'all cryptos']:
            self.list_cryptos()
            return True
        
        # Pattern matching for queries
        if 'sustainable' in query or 'eco' in query or 'green' in query:
            self.recommend_sustainable()
        elif 'rising' in query or 'trending' in query or 'going up' in query:
            self.recommend_profitable()
        elif 'long-term' in query or 'long term' in query or 'future' in query:
            self.recommend_long_term()
        elif 'compare' in query or 'vs' in query or ' and ' in query:
            self.compare_cryptos(query)
        elif 'low energy' in query or 'energy efficient' in query:
            self.find_low_energy()
        elif 'about' in query or 'tell me' in query or 'info' in query:
            # Extract crypto name
            for name in crypto_db.keys():
                if name.lower() in query:
                    self.get_crypto_details(name)
                    break
            else:
                print("\n❓ Which cryptocurrency would you like to know about?\n")
        else:
            print("\n🤔 Hmm, I'm not sure what you're asking.")
            print("Type 'help' to see example questions!\n")
        
        # Add disclaimer
        if self.conversation_count % 3 == 0:
            print("⚠️  Reminder: Crypto is risky—always do your own research! 💡\n")
        
        self.conversation_count += 1
        return True
    
    def run(self):
        """Main chatbot loop"""
        self.greet()
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                
                if not self.process_query(user_input):
                    print(f"\n👋 Thanks for chatting! Stay crypto-savvy! 🚀\n")
                    break
                    
            except KeyboardInterrupt:
                print(f"\n\n👋 Goodbye! Happy investing! 💰\n")
                break
            except Exception as e:
                print(f"\n❌ Oops! Something went wrong: {e}\n")

# Run the chatbot
if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.run()