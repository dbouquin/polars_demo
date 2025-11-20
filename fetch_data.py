"""
Fetch WASP-18 b phase-folded light curve data from STScI API

This script downloads the TESS light curve data for the exoplanet WASP-18 b
and saves it to a CSV file for use in the Polars tutorial.

Data source: STScI Exoplanet Archive (https://exo.mast.stsci.edu)
Target: WASP-18 b (TIC 100100827)
"""

import requests
import pandas as pd 

def fetch_wasp18_lightcurve():
    """
    Fetch phase-folded light curve data for WASP-18 b.
    
    Returns:
        pandas.DataFrame: DataFrame with columns PHASE, LC_DETREND, MODEL_INIT
    """
    # API endpoints
    planeturl = "https://exo.mast.stsci.edu/api/v0.1/exoplanets/"
    dvurl = "https://exo.mast.stsci.edu/api/v0.1/dvdata/tess/"
    header = {}
    
    print("Fetching planet identifiers for WASP-18 b...")
    
    # Get planet identifiers
    planet_name = "WASP-18 b"
    url = planeturl + "/identifiers/"
    myparams = {"name": planet_name}
    r = requests.get(url=url, params=myparams, headers=header)
    
    if r.status_code != 200:
        raise Exception(f"Failed to fetch planet identifiers: {r.status_code}")
    
    planet_names = r.json()
    ticid = planet_names['tessID']
    tce = planet_names['tessTCE']
    
    print(f"  TIC ID: {ticid}")
    print(f"  TCE: {tce}")
    
    # Get available sectors
    print("\nFetching available sectors...")
    url = dvurl + str(ticid) + '/tces/'
    myparams = {"tce": tce}
    r = requests.get(url=url, params=myparams, headers=header)
    
    if r.status_code != 200:
        raise Exception(f"Failed to fetch sector information: {r.status_code}")
    
    sectorInfo = r.json()
    sectors = [x[:11] for x in sectorInfo["TCE"] if tce in x]
    print(f"  Available sectors: {sectors}")
    print(f"  Using sector: {sectors[0]}")
    
    # Get the light curve data
    print("\nFetching light curve data...")
    url = dvurl + str(ticid) + '/table/'
    myparams = {"tce": tce, "sector": sectors[0]}
    r = requests.get(url=url, params=myparams, headers=header)
    
    if r.status_code != 200:
        raise Exception(f"Failed to fetch light curve data: {r.status_code}")
    
    tce_data = r.json()
    data = pd.DataFrame.from_dict(tce_data['data'])
    
    print(f"  Retrieved {len(data)} data points")
    print(f"  Columns: {list(data.columns)}")
    
    return data

def save_to_csv(data, filename="wasp18b_lightcurve.csv"):
    """
    Save the light curve data to a CSV file.
    
    Args:
        data: pandas DataFrame with light curve data
        filename: output filename (default: wasp18b_lightcurve.csv)
    """
    print(f"\nSaving data to {filename}...")
    data.to_csv(filename, index=False)
    print(f"  Saved {len(data)} rows")
    
    # Print some basic statistics
    print("\nData summary:")
    print(f"  Phase range: {data['PHASE'].min():.4f} to {data['PHASE'].max():.4f} days")
    print(f"  Flux range: {data['LC_DETREND'].min():.6f} to {data['LC_DETREND'].max():.6f}")
    print(f"  File size: {data.memory_usage(deep=True).sum() / 1024:.2f} KB")

if __name__ == "__main__":
    print("=" * 60)
    print("WASP-18 b Light Curve Data Fetcher")
    print("=" * 60)
    
    try:
        # Fetch the data
        lightcurve_data = fetch_wasp18_lightcurve()
        
        # Save to CSV
        save_to_csv(lightcurve_data)
        
        print("\n" + "=" * 60)
        print("SUCCESS! Data ready for Polars tutorial")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nERROR: {e}")
        print("Data fetch failed. Please check your internet connection and try again.")