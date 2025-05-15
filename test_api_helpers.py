"""
Test script for the updated API_helpers.py
This is a simple script to demonstrate how to use the updated API
with different picture count configurations.
"""
from API_helpers import get_tokyo_pics, get_rome_pics, get_paris_pics, get_dubai_pics, get_egypt_pics

def test_api_helpers():
    """Test the updated API helpers with different picture counts"""
    print("Testing API helpers with different picture counts\n")

    # Test Tokyo with default number of pictures (10)
    print("Tokyo pictures (default):")
    tokyo_pics = get_tokyo_pics()
    print(f"Retrieved {len(tokyo_pics)} pictures")
    
    # Test Rome with 5 pictures
    print("\nRome pictures (max 5):")
    rome_pics = get_rome_pics(max_pics=5)
    print(f"Retrieved {len(rome_pics)} pictures")
    
    # Test Paris with 15 pictures (will return up to available pictures)
    print("\nParis pictures (max 15):")
    paris_pics = get_paris_pics(max_pics=15)
    print(f"Retrieved {len(paris_pics)} pictures")
    
    # Test Dubai with 3 pictures
    print("\nDubai pictures (max 3):")
    dubai_pics = get_dubai_pics(max_pics=3)
    print(f"Retrieved {len(dubai_pics)} pictures")
    
    # Test Egypt with 8 pictures
    print("\nEgypt pictures (max 8):")
    egypt_pics = get_egypt_pics(max_pics=8)
    print(f"Retrieved {len(egypt_pics)} pictures")

if __name__ == "__main__":
    test_api_helpers()