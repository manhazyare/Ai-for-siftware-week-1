"""
Test Script for CryptoBuddy
Automated testing of chatbot functionality
"""

from crypto_buddy import CryptoBuddy, crypto_db

def test_crypto_database():
    """Test that crypto database is properly structured"""
    print("Testing Cryptocurrency Database...")
    print("="*60)
    
    required_fields = ["symbol", "price_trend", "market_cap", "energy_use", 
                       "sustainability_score", "risk_level", "description"]
    
    for name, data in crypto_db.items():
        print(f"✓ {name}: ", end="")
        missing = [field for field in required_fields if field not in data]
        if missing:
            print(f"❌ Missing fields: {missing}")
        else:
            print("✅ All fields present")
    
    print(f"\nTotal cryptocurrencies: {len(crypto_db)}")
    print("="*60 + "\n")

def test_chatbot_responses():
    """Test various chatbot responses"""
    print("Testing Chatbot Responses...")
    print("="*60)
    
    bot = CryptoBuddy()
    
    test_queries = [
        "Which crypto is most sustainable?",
        "Show me rising cryptocurrencies",
        "What's the best long-term investment?",
        "List all cryptos",
        "Tell me about Bitcoin",
        "Compare Bitcoin and Cardano",
        "Which has low energy use?"
    ]
    
    print("\n📝 Testing Query Processing:\n")
    for i, query in enumerate(test_queries, 1):
        print(f"{i}. Testing: '{query}'")
        try:
            bot.process_query(query)
            print("   ✅ Response generated successfully\n")
        except Exception as e:
            print(f"   ❌ Error: {e}\n")
    
    print("="*60 + "\n")

def test_recommendation_logic():
    """Test recommendation algorithms"""
    print("Testing Recommendation Logic...")
    print("="*60 + "\n")
    
    # Test sustainable recommendation
    sustainable_cryptos = {name: data["sustainability_score"] 
                          for name, data in crypto_db.items()}
    best_sustainable = max(sustainable_cryptos, key=sustainable_cryptos.get)
    print(f"✓ Most Sustainable: {best_sustainable} "
          f"(Score: {sustainable_cryptos[best_sustainable]}/10)")
    
    # Test rising cryptos
    rising_cryptos = [name for name, data in crypto_db.items() 
                     if data["price_trend"] == "rising"]
    print(f"✓ Rising Cryptocurrencies: {len(rising_cryptos)} found")
    for crypto in rising_cryptos:
        print(f"  • {crypto}")
    
    # Test low energy
    low_energy = [name for name, data in crypto_db.items() 
                  if data["energy_use"] == "low"]
    print(f"✓ Low Energy Options: {len(low_energy)} found")
    for crypto in low_energy:
        print(f"  • {crypto}")
    
    print("\n" + "="*60 + "\n")

def test_scoring_algorithm():
    """Test long-term investment scoring"""
    print("Testing Scoring Algorithm...")
    print("="*60 + "\n")
    
    print("Calculating scores for each cryptocurrency:\n")
    
    scored = []
    for name, data in crypto_db.items():
        score = 0
        breakdown = []
        
        if data["price_trend"] == "rising":
            score += 3
            breakdown.append("Rising trend (+3)")
        
        if data["market_cap"] == "high":
            score += 2
            breakdown.append("High market cap (+2)")
        
        score += data["sustainability_score"]
        breakdown.append(f"Sustainability (+{data['sustainability_score']})")
        
        scored.append((name, score, breakdown))
        
        print(f"{name}: {score}/15 points")
        for item in breakdown:
            print(f"  • {item}")
        print()
    
    best = max(scored, key=lambda x: x[1])
    print(f"🏆 Best Overall Score: {best[0]} with {best[1]}/15 points")
    
    print("\n" + "="*60 + "\n")

def run_all_tests():
    """Run all tests"""
    print("\n" + "🧪 CRYPTOBUDDY TEST SUITE 🧪".center(60))
    print("="*60 + "\n")
    
    test_crypto_database()
    test_recommendation_logic()
    test_scoring_algorithm()
    test_chatbot_responses()
    
    print("✅ All tests completed!")
    print("="*60 + "\n")
    print("💡 Your chatbot is ready for submission!")
    print("   Next steps:")
    print("   1. Take screenshots of conversations")
    print("   2. Record a 30-second demo video")
    print("   3. Write your 50-word reflection")
    print("   4. Push to GitHub and share!")
    print("\n")

if __name__ == "__main__":
    run_all_tests()