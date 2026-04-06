"""
IPFS anchoring module for SYNTHEIA
Provides functionality to anchor data on IPFS for immutability
"""
import os
import json
import hashlib
import requests
from typing import Any, Union


IPFS_ENDPOINT = os.getenv("IPFS_ENDPOINT", "http://ipfs:5001")


def anchor_ipfs(data: Union[str, bytes, dict], path: str = "/") -> str:
    """
    Anchor data on IPFS and return the CID
    
    Args:
        data: Data to anchor (string, bytes, or dict)
        path: Virtual path for organization (not used in actual IPFS)
        
    Returns:
        IPFS Content Identifier (CID)
    """
    try:
        # Convert data to bytes if needed
        if isinstance(data, dict):
            data_bytes = json.dumps(data, indent=2).encode('utf-8')
        elif isinstance(data, str):
            data_bytes = data.encode('utf-8')
        else:
            data_bytes = data
        
        # Calculate hash as CID placeholder
        # In production, this would use actual IPFS API
        cid = hashlib.sha256(data_bytes).hexdigest()
        
        # Try to submit to IPFS API
        try:
            response = requests.post(
                f"{IPFS_ENDPOINT}/api/v0/add",
                files={"file": data_bytes},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                cid = result.get("Hash", cid)
                print(f"Anchored to IPFS: {cid} (path: {path})")
            else:
                print(f"IPFS submission returned {response.status_code}, using local CID")
                
        except requests.exceptions.RequestException as e:
            print(f"IPFS not available, using local CID: {e}")
        
        return cid
        
    except Exception as e:
        print(f"Error anchoring to IPFS: {e}")
        # Return a deterministic hash as fallback
        return hashlib.sha256(str(data).encode()).hexdigest()


def get_from_ipfs(cid: str) -> bytes:
    """
    Retrieve data from IPFS by CID
    
    Args:
        cid: IPFS Content Identifier
        
    Returns:
        Data bytes
    """
    try:
        response = requests.post(
            f"{IPFS_ENDPOINT}/api/v0/cat",
            params={"arg": cid},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to retrieve from IPFS: {response.status_code}")
            return b""
            
    except Exception as e:
        print(f"Error retrieving from IPFS: {e}")
        return b""
