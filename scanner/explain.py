def explain_results(results):
    explanations = {}

    # Public Access Block
    pab = results.get("public_access_block", {})
    if "error" in pab:
        explanations["public_access_block"] = f"⚠️ {pab['error']}"
    elif all([
        pab.get("BlockPublicAcls") is True,
        pab.get("IgnorePublicAcls") is True,
        pab.get("BlockPublicPolicy") is True,
        pab.get("RestrictPublicBuckets") is True
    ]):
        explanations["public_access_block"] = "✅ Public access is blocked."
    else:
        explanations["public_access_block"] = "❌ Public access is NOT fully blocked."

    # Encryption
    enc = results.get("encryption", {})
    if "error" in enc:
        explanations["encryption"] = f"❌ {enc['error']}"
    else:
        try:
            rules = enc.get("Rules", [])
            if rules and rules[0].get("ApplyServerSideEncryptionByDefault", {}).get("SSEAlgorithm"):
                explanations["encryption"] = "✅ Bucket is encrypted."
            else:
                explanations["encryption"] = "❌ Bucket is not encrypted."
        except Exception:
            explanations["encryption"] = "❌ Unable to determine encryption."

    # Policy Status
    policy = results.get("policy_status", {})
    if "error" in policy:
        explanations["policy_status"] = f"⚠️ {policy['error']}"
    else:
        is_public = policy.get("IsPublic")
        if is_public is False:
            explanations["policy_status"] = "✅ Bucket policy is private."
        elif is_public is True:
            explanations["policy_status"] = "❌ Bucket policy allows public access."
        else:
            explanations["policy_status"] = "⚠️ Unable to determine policy status."

    return explanations

