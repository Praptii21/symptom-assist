import asyncio
from httpx import AsyncClient

async def test_session_persistence():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        print("\n--- TEST 1: Initial Symptom (Fever) ---")
        payload1 = {
            "messages": [{"role": "user", "content": "I have a fever"}],
            "session_id": None
        }
        response1 = await ac.post("/chat", json=payload1)
        data1 = response1.json()
        
        session_id = data1["session_id"]
        symptoms1 = data1["extracted_symptoms"]
        
        print(f"Status: {response1.status_code}")
        print(f"Session ID: {session_id}")
        print(f"Symptoms: {symptoms1}")
        
        assert "fever" in symptoms1
        assert session_id is not None

        print("\n--- TEST 2: Follow-up Symptom (Headache) with same Session ID ---")
        payload2 = {
            "messages": [
                {"role": "user", "content": "I have a fever"},
                {"role": "assistant", "content": data1["reply"]},
                {"role": "user", "content": "Also, I have a headache"}
            ],
            "session_id": session_id
        }
        response2 = await ac.post("/chat", json=payload2)
        data2 = response2.json()
        
        symptoms2 = data2["extracted_symptoms"]
        print(f"Status: {response2.status_code}")
        print(f"Session ID (echoed): {data2['session_id']}")
        print(f"Merged Symptoms: {symptoms2}")
        
        assert "fever" in symptoms2
        assert "headache" in symptoms2
        assert data2["session_id"] == session_id
        print("\n✅ SUCCESS: Session persistence is working correctly!")

if __name__ == "__main__":
    asyncio.run(test_session_persistence())
