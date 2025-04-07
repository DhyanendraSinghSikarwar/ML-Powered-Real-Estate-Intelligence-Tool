  from geopy.geocoders import Nominatim
  import pandas as pd
  import time

  # Initialize Nominatim (OpenStreetMap's geocoder)
  geolocator = Nominatim(user_agent="gurugram_sector_locator")

  def get_coordinates(sector):
      """Fetch latitude and longitude for a sector in Gurugram using OpenStreetMap."""
      location = f"Sector {sector}, Gurugram, India"
      try:
          # Add delay to avoid rate limits (1 request per second)
          time.sleep(1)
          
          # Fetch location data
          result = geolocator.geocode(location, exactly_one=True)
          
          if result:
              return f"{result.latitude:.6f}° N, {result.longitude:.6f}° E"
          else:
              print(f"⚠️ No coordinates found for Sector {sector}")
              return None
      except Exception as e:
          print(f"❌ Error fetching Sector {sector}: {e}")
          return None

  # Create DataFrame to store results
  df = pd.DataFrame(columns=['Sector', 'Coordinates'])

  # Fetch coordinates for sectors 1 to 115
  for sector in range(1, 116):
      coordinates = get_coordinates(sector)
      df = pd.concat([df, pd.DataFrame({'Sector': [sector], 'Coordinates': [coordinates]})], ignore_index=True)
      print(f"Sector {sector}: {coordinates}")

  # Save results to CSV
  df.to_csv('gurugram_sector_coordinates.csv', index=False)
  print("✅ Data saved to 'gurugram_sector_coordinates.csv'")