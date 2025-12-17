<<<<<<< HEAD
import streamlit as st
from datetime import datetime

from scoring.evidence import evidence_quality_score
from scoring.contradiction import contradiction_score
from scoring.novelty import novelty_score
from scoring.market import market_need_score
from scoring.final_score import final_confidence


# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="VaidyaNext | EY Techathon Prototype",
    layout="wide"
)

# ===================== HEADER =====================
st.title("🧪 VaidyaNext — AI-Powered Drug Discovery & R&D Companion")

st.markdown(
    """
    **VaidyaNext is a Decision Intelligence platform designed to de-risk
    Pharmaceutical R&D by transforming fragmented scientific evidence
    into a single, explainable confidence score.**

    This working prototype demonstrates how AI-assisted analysis can help
    R&D teams **decide what to pursue, what to pause, and what to avoid** —
    reducing evaluation cycles from months to minutes.
    """
)

st.markdown("---")


# ===================== CONTEXT: WHAT THIS PROTOTYPE DOES =====================
with st.expander("📌 What does this prototype demonstrate? (Read this first)"):
    st.markdown(
        """
        This prototype demonstrates:
        - A **working decision pipeline** for Pharma R&D evaluation  
        - Live execution of our **6-D Framework**  
        - Transparent scoring and **explainable recommendations**  
        - A **demonstratable technology output**, as required for EY Techathon Round-2  

        ⚠️ *All data used is simulated for demonstration purposes.*
        """
    )


# ===================== INPUT SECTION =====================
st.subheader("🔍 Research Input")

col_input_1, col_input_2 = st.columns(2)

with col_input_1:
    disease = st.text_input(
        "🧬 Disease / Indication",
        placeholder="e.g. Alzheimer, Blood Cancer"
    )

with col_input_2:
    drug = st.text_input(
        "💊 Drug / Compound Name",
        placeholder="e.g. VX-101, Paracetamol"
    )

st.markdown("---")


# ===================== SIMULATED DATA INGESTION =====================
sample_papers = [
    "Randomized controlled trial showed improved outcomes with large sample size",
    "Meta-analysis found no effect in certain populations",
    "Double blind controlled trial with 300 patients showed significant benefit"
]


# ===================== RUN ANALYSIS =====================
if st.button("🚀 Run 6-D Analysis"):

    # ---------- CORE SCORING ----------
    evidence = evidence_quality_score(sample_papers)
    contradiction = contradiction_score(sample_papers)
    novelty = novelty_score(drug)
    market = market_need_score(disease)

    final = final_confidence(
        evidence=evidence,
        contradiction=contradiction,
        novelty=novelty,
        market=market
    )

    # ===================== RESEARCH CONTEXT =====================
    st.subheader("📌 Research Context")

    ctx1, ctx2 = st.columns(2)
    ctx1.info(f"**Disease Target:** {disease or 'Not specified'}")
    ctx2.info(f"**Proposed Drug / Compound:** {drug or 'Not specified'}")

    st.markdown("---")


    # ===================== DASHBOARD =====================
    st.subheader("📊 6-D Analysis Dashboard")

    d1, d2, d3, d4 = st.columns(4)

    d1.metric("Evidence Quality", evidence)
    d1.progress(evidence)

    d2.metric("Contradiction Score", contradiction)
    d2.progress(contradiction)

    d3.metric("Novelty Score", novelty)
    d3.progress(novelty)

    d4.metric("Market Need Index", market)
    d4.progress(market)


    # ===================== SCORE EXPLANATION =====================
    with st.expander("📘 Explanation of Scores (Methodology Reference)"):
        st.markdown(
            f"""
            **Evidence Quality (D3 – Distill)**  
            Evaluates strength of scientific literature based on study design,
            trial rigor, and sample size indicators.  
            **Current Score:** `{evidence}`

            **Contradiction Score (D2 – Decode)**  
            Detects conflicting outcomes across research papers to highlight
            scientific uncertainty.  
            **Current Score:** `{contradiction}`

            **Novelty Score (D4 – Differentiate)**  
            Estimates originality and patent risk by identifying overlap with
            known or generic compounds *(simulated)*.  
            **Current Score:** `{novelty}`

            **Market Need Index (D5 – Demand)**  
            Assesses unmet medical and commercial demand for the target indication.  
            **Current Score:** `{market}`
            """
        )

    st.markdown("---")


    # ===================== FINAL DECISION =====================
    st.subheader("🔍 Final Confidence Score (D6 – Decide)")
    st.metric("Overall R&D Confidence Score", final)

    if final >= 75:
        decision = "✅ Proceed with R&D"
        st.success(decision)
    elif final >= 50:
        decision = "⚠️ Re-evaluate Strategy"
        st.warning(decision)
    else:
        decision = "❌ High Risk – Do Not Proceed"
        st.error(decision)


    # ===================== DECISION RATIONALE =====================
    st.subheader("🧠 Decision Rationale")

    rationale = []

    if evidence >= 70:
        rationale.append("Strong evidence quality from high-quality studies.")
    else:
        rationale.append("Limited or moderate strength of scientific evidence.")

    if contradiction >= 60:
        rationale.append("Significant contradictory outcomes detected across literature.")
    else:
        rationale.append("Relatively consistent findings across studies.")

    if novelty < 50:
        rationale.append("Low novelty due to existing widespread or generic drug usage.")
    else:
        rationale.append("High novelty with reduced patent or originality risk.")

    if market >= 70:
        rationale.append("High unmet medical or commercial need identified.")
    else:
        rationale.append("Moderate to low unmet market demand.")

    for point in rationale:
        st.write("•", point)


    # ===================== HOW TO IMPROVE =====================
    with st.expander("📈 How can this R&D confidence be improved?"):
        st.markdown(
            """
            • Reduce contradictions by targeting specific patient sub-populations  
            • Improve novelty through molecule modification or new mechanisms  
            • Strengthen evidence via larger, well-designed trials  
            • Focus on indications with higher unmet medical need  
            """
        )


    # ===================== CONFIDENCE BANDS =====================
    with st.expander("📊 Confidence Bands (Decision Governance)"):
        st.markdown(
            """
            🟢 **75 – 100** → Proceed with R&D  
            🟡 **50 – 74** → Re-evaluate Strategy  
            🔴 **Below 50** → High Risk – Do Not Proceed  
            """
        )


    # ===================== 6-D FRAMEWORK =====================
    with st.expander("🧩 Live Mapping to the VaidyaNext 6-D Framework"):
        st.markdown(
            """
            **D1 – Discover:** Relevant research identification *(simulated ingestion)*  
            **D2 – Decode:** Extraction of key outcomes and signals  
            **D3 – Distill:** Evidence Quality Scoring  
            **D4 – Differentiate:** Novelty & patent risk estimation  
            **D5 – Demand:** Market Need Index  
            **D6 – Decide:** Final Confidence Score  
            """
        )


    # ===================== FOOTER =====================
    st.markdown("---")
    st.caption(
        f"Prototype Mode — Simulated data for demonstration only | Generated on {datetime.now().strftime('%d %b %Y, %H:%M')}"
    )
=======
import streamlit as st
from datetime import datetime

from scoring.evidence import evidence_quality_score
from scoring.contradiction import contradiction_score
from scoring.novelty import novelty_score
from scoring.market import market_need_score
from scoring.final_score import final_confidence


# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="VaidyaNext | EY Techathon Prototype",
    layout="wide"
)

# ===================== HEADER =====================
st.title("🧪 VaidyaNext — AI-Powered Drug Discovery & R&D Companion")

st.markdown(
    """
    **VaidyaNext is a Decision Intelligence platform designed to de-risk
    Pharmaceutical R&D by transforming fragmented scientific evidence
    into a single, explainable confidence score.**

    This working prototype demonstrates how AI-assisted analysis can help
    R&D teams **decide what to pursue, what to pause, and what to avoid** —
    reducing evaluation cycles from months to minutes.
    """
)

st.markdown("---")


# ===================== CONTEXT: WHAT THIS PROTOTYPE DOES =====================
with st.expander("📌 What does this prototype demonstrate? (Read this first)"):
    st.markdown(
        """
        This prototype demonstrates:
        - A **working decision pipeline** for Pharma R&D evaluation  
        - Live execution of our **6-D Framework**  
        - Transparent scoring and **explainable recommendations**  
        - A **demonstratable technology output**, as required for EY Techathon Round-2  

        ⚠️ *All data used is simulated for demonstration purposes.*
        """
    )


# ===================== INPUT SECTION =====================
st.subheader("🔍 Research Input")

col_input_1, col_input_2 = st.columns(2)

with col_input_1:
    disease = st.text_input(
        "🧬 Disease / Indication",
        placeholder="e.g. Alzheimer, Blood Cancer"
    )

with col_input_2:
    drug = st.text_input(
        "💊 Drug / Compound Name",
        placeholder="e.g. VX-101, Paracetamol"
    )

st.markdown("---")


# ===================== SIMULATED DATA INGESTION =====================
sample_papers = [
    "Randomized controlled trial showed improved outcomes with large sample size",
    "Meta-analysis found no effect in certain populations",
    "Double blind controlled trial with 300 patients showed significant benefit"
]


# ===================== RUN ANALYSIS =====================
if st.button("🚀 Run 6-D Analysis"):

    # ---------- CORE SCORING ----------
    evidence = evidence_quality_score(sample_papers)
    contradiction = contradiction_score(sample_papers)
    novelty = novelty_score(drug)
    market = market_need_score(disease)

    final = final_confidence(
        evidence=evidence,
        contradiction=contradiction,
        novelty=novelty,
        market=market
    )

    # ===================== RESEARCH CONTEXT =====================
    st.subheader("📌 Research Context")

    ctx1, ctx2 = st.columns(2)
    ctx1.info(f"**Disease Target:** {disease or 'Not specified'}")
    ctx2.info(f"**Proposed Drug / Compound:** {drug or 'Not specified'}")

    st.markdown("---")


    # ===================== DASHBOARD =====================
    st.subheader("📊 6-D Analysis Dashboard")

    d1, d2, d3, d4 = st.columns(4)

    d1.metric("Evidence Quality", evidence)
    d1.progress(evidence)

    d2.metric("Contradiction Score", contradiction)
    d2.progress(contradiction)

    d3.metric("Novelty Score", novelty)
    d3.progress(novelty)

    d4.metric("Market Need Index", market)
    d4.progress(market)


    # ===================== SCORE EXPLANATION =====================
    with st.expander("📘 Explanation of Scores (Methodology Reference)"):
        st.markdown(
            f"""
            **Evidence Quality (D3 – Distill)**  
            Evaluates strength of scientific literature based on study design,
            trial rigor, and sample size indicators.  
            **Current Score:** `{evidence}`

            **Contradiction Score (D2 – Decode)**  
            Detects conflicting outcomes across research papers to highlight
            scientific uncertainty.  
            **Current Score:** `{contradiction}`

            **Novelty Score (D4 – Differentiate)**  
            Estimates originality and patent risk by identifying overlap with
            known or generic compounds *(simulated)*.  
            **Current Score:** `{novelty}`

            **Market Need Index (D5 – Demand)**  
            Assesses unmet medical and commercial demand for the target indication.  
            **Current Score:** `{market}`
            """
        )

    st.markdown("---")


    # ===================== FINAL DECISION =====================
    st.subheader("🔍 Final Confidence Score (D6 – Decide)")
    st.metric("Overall R&D Confidence Score", final)

    if final >= 75:
        decision = "✅ Proceed with R&D"
        st.success(decision)
    elif final >= 50:
        decision = "⚠️ Re-evaluate Strategy"
        st.warning(decision)
    else:
        decision = "❌ High Risk – Do Not Proceed"
        st.error(decision)


    # ===================== DECISION RATIONALE =====================
    st.subheader("🧠 Decision Rationale")

    rationale = []

    if evidence >= 70:
        rationale.append("Strong evidence quality from high-quality studies.")
    else:
        rationale.append("Limited or moderate strength of scientific evidence.")

    if contradiction >= 60:
        rationale.append("Significant contradictory outcomes detected across literature.")
    else:
        rationale.append("Relatively consistent findings across studies.")

    if novelty < 50:
        rationale.append("Low novelty due to existing widespread or generic drug usage.")
    else:
        rationale.append("High novelty with reduced patent or originality risk.")

    if market >= 70:
        rationale.append("High unmet medical or commercial need identified.")
    else:
        rationale.append("Moderate to low unmet market demand.")

    for point in rationale:
        st.write("•", point)


    # ===================== HOW TO IMPROVE =====================
    with st.expander("📈 How can this R&D confidence be improved?"):
        st.markdown(
            """
            • Reduce contradictions by targeting specific patient sub-populations  
            • Improve novelty through molecule modification or new mechanisms  
            • Strengthen evidence via larger, well-designed trials  
            • Focus on indications with higher unmet medical need  
            """
        )


    # ===================== CONFIDENCE BANDS =====================
    with st.expander("📊 Confidence Bands (Decision Governance)"):
        st.markdown(
            """
            🟢 **75 – 100** → Proceed with R&D  
            🟡 **50 – 74** → Re-evaluate Strategy  
            🔴 **Below 50** → High Risk – Do Not Proceed  
            """
        )


    # ===================== 6-D FRAMEWORK =====================
    with st.expander("🧩 Live Mapping to the VaidyaNext 6-D Framework"):
        st.markdown(
            """
            **D1 – Discover:** Relevant research identification *(simulated ingestion)*  
            **D2 – Decode:** Extraction of key outcomes and signals  
            **D3 – Distill:** Evidence Quality Scoring  
            **D4 – Differentiate:** Novelty & patent risk estimation  
            **D5 – Demand:** Market Need Index  
            **D6 – Decide:** Final Confidence Score  
            """
        )


    # ===================== FOOTER =====================
    st.markdown("---")
    st.caption(
        f"Prototype Mode — Simulated data for demonstration only | Generated on {datetime.now().strftime('%d %b %Y, %H:%M')}"
    )
>>>>>>> ac9c0be07e6f28600dff7f2ebe59dd2e585ab10a
