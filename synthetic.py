import os

paths = [
    "jawahar_estate_rag_data/company_overview",
    "jawahar_estate_rag_data/properties/residential_properties",
    "jawahar_estate_rag_data/properties/commercial_properties",
    "jawahar_estate_rag_data/properties/luxury_properties",
    "jawahar_estate_rag_data/pricing/pricing_model",
    "jawahar_estate_rag_data/pricing/rent_vs_buy_analysis",
    "jawahar_estate_rag_data/legal_compliance/property_laws",
    "jawahar_estate_rag_data/legal_compliance/buyer_requirements",
    "jawahar_estate_rag_data/legal_compliance/rental_agreements",
    "jawahar_estate_rag_data/market_insights/market_trends_2025",
    "jawahar_estate_rag_data/market_insights/location_analysis",
    "jawahar_estate_rag_data/customer_support/faq",
    "jawahar_estate_rag_data/customer_support/contact_process",
    "jawahar_estate_rag_data/internal_policies/data_privacy",
    "jawahar_estate_rag_data/internal_policies/agent_guidelines"
]

for path in paths:
    os.makedirs(path, exist_ok=True)
print("Structure created!")
