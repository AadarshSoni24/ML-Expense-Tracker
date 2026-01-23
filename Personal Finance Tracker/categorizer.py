from ml_categorizer import predict_category
def categorize(description):
    # Try ML-based categorization first
    try:
        return predict_category(description)
    except:
        # Fallback to rule-based categorization
        desc = description.lower()

        if "zomato" in desc or "swiggy" in desc:
            return "Food"
        elif "uber" in desc or "ola" in desc:
            return "Transport"
        elif "netflix" in desc or "spotify" in desc:
            return "Subscriptions"
        elif "salary" in desc:
            return "Income"
        else:
            return "Other"
