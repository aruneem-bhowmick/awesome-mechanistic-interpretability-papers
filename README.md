# Awesome Mechanistic Interpretability Papers

A curated, **pedagogically ordered** reading list for mechanistic interpretability (mech interp), structured so you can start from first principles and work toward the current research frontier, rather than a flat alphabetical dump.

Each section is ordered **foundational → detailed/advanced**. If you're new to the field, read sections 1–3 in order before branching out. If you're already fluent, jump straight to 4–9 for the research-frontier material.

> Contributions welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Table of Contents

1. [Foundations & Philosophy](#1-foundations--philosophy)
2. [Circuits & Features](#2-circuits--features)
3. [Superposition & Sparse Autoencoders](#3-superposition--sparse-autoencoders)
4. [Representation Geometry & Linear Structure](#4-representation-geometry--linear-structure)
5. [Causal Methods: Patching, Ablation, Editing](#5-causal-methods-patching-ablation-editing)
6. [In-Context Learning & Attention Circuits](#6-in-context-learning--attention-circuits)
7. [Training Dynamics & Grokking](#7-training-dynamics--grokking)
8. [Scaling Interpretability & Automated Interp](#8-scaling-interpretability--automated-interp)
9. [Applications: Safety, Steering, Unlearning](#9-applications-safety-steering-unlearning)
10. [Surveys & Reviews](#10-surveys--reviews)
11. [Tools & Libraries](#11-tools--libraries)

---

## 1. Foundations & Philosophy

Start here. These establish *why* mech interp is a coherent research program and the vocabulary everything else builds on.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/) | Olah, Cammarata, Schubert, Goh, Petrov, Carter (OpenAI/Distill) | 2020 | The founding manifesto: features and circuits as the basic units of understanding, built on vision models. Sets the epistemic stance the whole field inherits. |
| [An Overview of Early Vision in InceptionV1](https://distill.pub/2020/circuits/early-vision/) | Olah et al. (Distill) | 2020 | Companion piece; shows exhaustive circuit-level analysis is possible for a full subsystem, not just cherry-picked units. |
| [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html) | Elhage et al. (Anthropic) | 2021 | The Rosetta Stone for transformer mech interp: QK/OV circuits, the residual stream as shared communication channel, induction heads' first appearance. Read this before anything else on transformers. |
| [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) | Elhage et al. (Anthropic) | 2022 | Explains *why* neurons are polysemantic: models represent more features than they have dimensions. Motivates nearly everything in Section 3. |
| [Thinking About Risks From AI: Accident, Misuse and Structure](https://www.governance.ai/research-paper/thinking-about-risks-from-ai-accidents-misuse-and-structure) | Zwetsloot & Dafoe (context piece, not required but useful) | 2019 | Optional context for why interpretability is treated as a safety-relevant research program, not just neuroscience-for-NNs. |

---

## 2. Circuits & Features

Concrete circuit-level case studies, the "detailed papers" the foundations point toward.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Interpretability in the Wild: A Circuit for Indirect Object Identification in GPT-2 Small](https://arxiv.org/abs/2211.00593) | Wang, Variengien, Conmy, Shlegeris, Steinhardt | 2022 | The canonical worked example of full circuit discovery in a language model: reverse-engineers a specific behavior end-to-end. |
| [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217) | Nanda, Chan, Lieberum, Smith, Steinhardt | 2023 | Reverse-engineers modular addition into a Fourier-multiplication circuit; bridges circuits work with training dynamics (see Section 7). |
| [Copy Suppression: Comprehensively Understanding an Attention Head](https://arxiv.org/abs/2310.04625) | McDougall, Conmy, Rushing, McGrath, Nanda | 2023 | A rigorous, complete case study of a single attention head's function: good template for how to write a circuits paper. |
| [Does Circuit Analysis Interpretability Scale? Evidence from Multiple Choice Capabilities in Chinchilla](https://arxiv.org/abs/2307.09458) | Lieberum, Rahtz, Kramár, Nanda, Irving, Shah, Varma | 2023 | Tests whether small-model circuit-analysis techniques transfer to a 70B model; honest about what breaks. |
| [Attribution Patching Outperforms Automated Circuit Discovery](https://arxiv.org/abs/2310.10348) | Kramár, Lieberum, Shah, Nanda | 2024 | Efficient gradient-based approximation to activation patching for circuit discovery at scale. |
| [Data-driven Circuit Discovery for Interpretability of Language Models](https://arxiv.org/abs/2605.09129) | Rai, Geva, Yao | 2026 | A data-driven alternative to hand-specified discovery templates, from authors who also survey the field in §10 — a different lever on the same problem Attribution Patching addresses. |
| [Demystifying Variance in Circuit Discovery of LLMs](https://arxiv.org/abs/2606.16920) | Wu, Tonin, Cevher | 2026 | Quantifies how much the current state-of-the-art discovery method (EAP-IG) varies across seeds and configuration choices — a reliability check the field needed once discovery moved from bespoke case studies like IOI to standardized pipelines. |
| [Many Circuits, One Mechanism: Input Variation and Evaluation Granularity in Circuit Discovery](https://arxiv.org/abs/2606.06267) | Makou, Niu, Dutta, Gurevych | 2026 | Tests the common assumption that structurally different discovered circuits imply different underlying mechanisms — a conceptual companion to Have Faith in Faithfulness (§5) aimed specifically at circuit discovery. |

*Extended reading: [`extended-reading/02-circuits-and-features.md`](extended-reading/02-circuits-and-features.md).*

---

## 3. Superposition & Sparse Autoencoders

The current dominant paradigm for extracting monosemantic features from superposed representations.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html) | Elhage et al. (Anthropic) | 2022 | (Cross-listed from §1: the theoretical setup SAEs are built to solve.) |
| [Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html) | Bricken et al. (Anthropic) | 2023 | First demonstration that sparse dictionary learning recovers interpretable, monosemantic features from a real language model. |
| [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600) | Cunningham, Ewart, Riggs, Huben, Sharkey | 2023 | Independent, concurrent confirmation of the SAE approach with careful interpretability metrics. |
| [Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet](https://transformer-circuits.pub/2024/scaling-monosemanticity/) | Templeton et al. (Anthropic) | 2024 | Scales SAEs to a production frontier model; introduces feature steering and abstraction hierarchies among features. |
| [Gemma Scope: Open Sparse Autoencoders Everywhere All At Once](https://arxiv.org/abs/2408.05147) | Lieberum et al. (Google DeepMind) | 2024 | Open-weights SAE suite across every layer of Gemma 2, the standard open benchmark resource for SAE research. |
| [Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models](https://arxiv.org/abs/2403.19647) | Marks, Rager, Michaud, Belinkov, Bau, Mueller | 2024 | Combines SAEs with circuit discovery: feature-level causal graphs rather than neuron-level. |
| [Interpretability Illusions in the Generalization of Simplified Models](https://arxiv.org/abs/2312.03656) | Friedman, Lampinen, Dixon, Chen, Ghandeharioun | 2023 | Important caution: simplified/probed representations can mislead about what the full model actually computes. Read alongside SAE optimism as a corrective. |
| [Measuring Monosemanticity in Sparse Autoencoders via Latent Activation Coherence](https://arxiv.org/abs/2607.17770) | Filus, Pokuciński | 2026 | Proposes an actual metric for monosemanticity rather than relying on human inspection of max-activating examples — fills a real evaluation-methodology gap left open by the papers above. |
| [Identifying Functionally Important Features with End-to-End Sparse Dictionary Learning](https://arxiv.org/abs/2405.12241) | Braun, Bushnaq, Heimersheim, Mendel, Sharkey | 2024 | Directly relevant to identifiability: asks whether SAE features are the *right* decomposition rather than just *a* sparse one. |
| [Are Single-Token Sparse Autoencoder Features Causally Necessary? Layer-Depth and SAE-Family Effects](https://arxiv.org/abs/2607.20596) | Cho, Wu, Costa, Kalra, Wicaksono, et al. | 2026 | The most current test of the identifiability question above: whether a feature's causal role holds up across SAE families and layer depth, not just within one trained dictionary. |

*Extended reading: [`extended-reading/03-superposition-and-saes.md`](extended-reading/03-superposition-and-saes.md).*

---

## 4. Representation Geometry & Linear Structure

The geometric/representational lens: how models encode information in the structure of activation space, as opposed to in discrete circuits.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Linear Algebraic Structure of Word Senses, with Applications to Polysemy](https://arxiv.org/abs/1601.03764) | Arora, Li, Liang, Ma, Risteski | 2018 | Early evidence for linear/additive structure in embeddings; precursor to the modern linear representation hypothesis. |
| [The Linear Representation Hypothesis and the Geometry of Large Language Models](https://arxiv.org/abs/2311.03658) | Park, Choe, Veitch | 2023 | Formalizes the linear representation hypothesis with a causal inner product; the clearest modern statement of the hypothesis in the current literature. |
| [Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task](https://arxiv.org/abs/2210.13382) | Li, Hopkins, Bau, Viégas, Pfister, Wattenberg | 2023 | Othello-GPT: clean evidence that transformers build structured, non-linguistic world models (board state) internally. |
| [Language Models Represent Space and Time](https://arxiv.org/abs/2310.02207) | Gurnee & Tegmark | 2023 | Linear probes recover literal spatiotemporal coordinates from LLM activations: geometry as a window onto world models. |
| [Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge across 18 Open-Source LLMs](https://arxiv.org/abs/2608.02486) | Chelombitko, Chelombitko, Hämäläinen | 2026 | Extends the probing tradition above to a new knowledge domain and adds a real caveat: a concept can be internally represented without being reliably decodable — worth reading before taking probe-based claims at face value. |
| [The Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987) | Huh, Cheung, Wang, Isola | 2024 | Argues independently trained models converge toward a shared representational geometry as scale increases: core reading for representational convergence research. |
| [Not All Language Model Features Are Linear](https://arxiv.org/abs/2405.14860) | Engels, Michaud, Liao, Gurnee, Tegmark | 2024 | Direct challenge to the linear representation hypothesis: finds circular/multi-dimensional features (e.g., day-of-week). Essential counterpoint to Park et al. |
| [Intertemporal Preference Steering in Qwen3 via Contrastive Activation Addition](https://arxiv.org/abs/2608.03892) | Mráz, Shenk | 2026 | A concrete, production-scale demonstration that linear representations (here, of temporal horizon) remain practically steerable even given the nonlinear counterexamples above — geometry theory cashed out as an intervention. |
| Geometry of Neural Network Loss Surfaces and Representations (survey-style framing, various authors; see Sec. 10) | N/A | N/A | See Surveys section for consolidated treatment. |

*Extended reading: [`extended-reading/04-representation-geometry.md`](extended-reading/04-representation-geometry.md).*

---

## 5. Causal Methods: Patching, Ablation, Editing

The empirical toolkit for testing whether a proposed circuit or feature is actually load-bearing.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Causal Abstractions of Neural Networks](https://arxiv.org/abs/2106.02997) | Geiger, Wu, Lu, Rozner, Kreiss, Icard, Goodman, Potts | 2021 | Formal causal-abstraction framework underlying activation patching: the theory before the technique became folklore. |
| [Locating and Editing Factual Associations in GPT (ROME)](https://arxiv.org/abs/2202.05262) | Meng, Bau, Andonian, Belinkov | 2022 | Causal tracing to localize factual recall to specific MLP layers, then direct weight editing: the template for causal-intervention-as-evidence. |
| [Mass-Editing Memory in a Transformer (MEMIT)](https://arxiv.org/abs/2210.07229) | Meng, Sharma, Andonian, Belinkov, Bau | 2023 | Scales ROME-style editing to thousands of facts simultaneously. |
| [How to Use and Interpret Activation Patching](https://arxiv.org/abs/2404.15255) | Heimersheim & Nanda | 2024 | Practical, opinionated methods paper: the "read this before you run your first patching experiment" reference. |
| [Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model Mechanisms](https://arxiv.org/abs/2403.17806) | Miller, Chughtai, Saunders | 2024 | Rigorously interrogates what "faithful" circuit explanations actually require: an important corrective against overclaiming from circuit-overlap results. |
| [Where Steering Signals Come From: Activation Source Selection in Activation Steering](https://arxiv.org/abs/2607.25270) | Ye, Ran, Yao, Wang, Jiang, et al. | 2026 | Extends the practical-methods lens of How to Use and Interpret Activation Patching to steering: the source of a steering vector is usually treated as an afterthought, and this shows it shouldn't be. |
| [Policy Gradient Steering: Interventions from Behavioral Objectives](https://arxiv.org/abs/2607.27574) | Poupart, Beynier, Maudet | 2026 | Shows existing vector-addition steering fails to steer even simple behaviors reliably, and proposes a policy-gradient alternative — a direct challenge to an assumption several other entries here take for granted. |
| [On the Generalization of Steering Vectors for Chain-of-Thought Faithfulness](https://arxiv.org/abs/2607.29062) | Nguyen, Cox, Meek, Arcuschin | 2026 | Tests whether steering vectors built for one setting generalize to CoT-faithfulness monitoring — a safety-relevant limit case for the technique above. |
| [A Few Neurons Reveal When LLMs Misuse Tools: Sparse Detection and Selective Steering for Reliable Tool Use](https://arxiv.org/abs/2608.00218) | Ke, Yin, Zhao, Huang | 2026 | A concrete, well-scoped detection-plus-intervention case study — sparse neuron-level detection followed by selective steering, in the spirit of Copy Suppression's single-mechanism rigor but for an applied failure mode. |

*Extended reading: [`extended-reading/05-causal-methods.md`](extended-reading/05-causal-methods.md).*

---

## 6. In-Context Learning & Attention Circuits

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | Olsson, Elhage, Nanda, Joseph, et al. (Anthropic) | 2022 | Identifies induction heads as a specific, mechanistically understood circuit responsible for a large fraction of in-context learning. |
| [Induction Heads Interpolate N-Grams](https://arxiv.org/abs/2607.02800) | D'Angelo, Yuksel, Narashiman, Flammarion | 2026 | A precise theoretical characterization of the estimator induction heads implement, sharpening the informal "copy-the-pattern" story above into something falsifiable. |
| [Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence](https://arxiv.org/abs/2606.12058) | Lavie, Fischer, Lekov, Maele, Ringel, et al. | 2026 | A training-dynamics account of *why* copy/induction heads emerge abruptly — connects the mechanism above to the grokking-adjacent emergence phenomena in §7. |
| [Necessary, Decodable and Reversible, Yet Not Transferable: A Stress Test for Attention-Head Role Claims](https://arxiv.org/abs/2606.08292) | Quirke | 2026 | Tests whether the standard evidence used to assign a role to an attention head (necessity, decodability, reversibility) actually implies that role transfers — a methodological caution specific to head-level claims, in the spirit of Have Faith in Faithfulness (§5). |
| [Through the Bottleneck: How Multi-head Latent Attention Separates Content from Position in Language Models](https://arxiv.org/abs/2607.23054) | Dhruvil S, Sojitra, Chauhan | 2026 | Extends mechanistic attention analysis to Multi-head Latent Attention (DeepSeek-V2's low-rank KV-cache mechanism) — the induction-heads story was built on vanilla attention; this checks whether it survives a widely-adopted architectural change. |
| [What Learning Algorithm Is In-Context Learning? Investigations with Linear Models](https://arxiv.org/abs/2211.15661) | Akyürek, Schuurmans, Andreas, Ma, Zhou | 2023 | Frames ICL as implicit gradient descent / algorithm selection: connects circuits work to a computational-mechanism hypothesis. |
| [Transformers Learn In-Context by Gradient Descent](https://arxiv.org/abs/2212.07677) | von Oswald et al. | 2023 | Constructive proof that transformers *can* implement gradient descent in a forward pass; complements Akyürek et al.'s empirical framing. |
| [Large language models reorganize representational geometry during in-context learning](https://arxiv.org/abs/2605.28854) | Xiong, Ji-An, Wilson, Lee, Wei | 2026 | Directly observes the geometric reorganization the algorithmic accounts above predict should happen — the missing empirical link between "ICL is an implicit algorithm" and representation geometry (§4). |
| [Function Vectors in Large Language Models](https://arxiv.org/abs/2310.15213) | Todd, Li, Sharma, Mueller, Wallace, Bau | 2024 | Shows ICL tasks are often represented as a single steerable "function vector" in the residual stream: a geometric, not just circuit, account of ICL. |
| [How Few-Shot Examples Add Up: A Causal Decomposition of Function Vectors in In-Context Learning](https://arxiv.org/abs/2605.16591) | Wang, Wang, Bakalova, Hahn | 2026 | Asks the natural next question after Function Vectors: how do individual few-shot examples causally combine to build that vector in the first place? |

*Extended reading: [`extended-reading/06-in-context-learning.md`](extended-reading/06-in-context-learning.md).*

---

## 7. Training Dynamics & Grokking

Covers how and when structured, generalizing computation emerges over the course of training, rather than only at convergence.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) | Power, Burda, Edwards, Babuschkin, Sutskever | 2022 | The original empirical discovery: sudden generalization long after training-set memorization. Sets up the puzzle. |
| [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217) | Nanda, Chan, Lieberum, Smith, Steinhardt | 2023 | (Cross-listed from §2.) Explains grokking mechanistically as gradual circuit formation masked by loss plateaus: essential bridge between geometry, circuits, and training dynamics. |
| [Omnigrok: Grokking Beyond Algorithmic Data](https://arxiv.org/abs/2210.01117) | Liu, Michaud, Tegmark | 2023 | Extends grokking to non-algorithmic tasks and gives a weight-norm-based explanation, broadening the phenomenon beyond toy settings. |
| [The Slingshot Mechanism: An Empirical Study of Adaptive Optimizer Training Dynamics](https://arxiv.org/abs/2206.04817) | Thilak, Litwin, Shao, Rabbani, Advani, Susskind | 2022 | Ties grokking-adjacent phenomena to optimizer instabilities: a training-dynamics-first (rather than representation-first) account worth contrasting with Nanda et al. |
| [Post-Grokking Collapse at the Representation-Readout Interface in Muon-Trained Transformers](https://arxiv.org/abs/2608.07436) | Janati, Maghraoui, Kanavalau, Belfatmi | 2026 | A direct, optimizer-specific extension of the Slingshot Mechanism's lens: Muon groks modular addition faster than AdamW, but the resulting solution doesn't hold — grokking speed and grokking robustness turn out to be different things. |
| [A Tale of Two Circuits: Grokking as Competition of Sparse and Dense Subnetworks](https://arxiv.org/abs/2303.11873) | Merrill, Tsilivis, Shukla | 2023 | Frames grokking as competition between a memorizing dense subnetwork and a generalizing sparse subnetwork: a useful lens for judging when a model has actually converged on a generalizing solution. |
| [Tunneling the Loss Landscape: Bypassing Memorization with Monte Carlo Parameter Swapping](https://arxiv.org/abs/2608.01833) | Chan, Zhang, Shang, Zhang, Yang | 2026 | Takes the memorization-vs-generalization framing above and turns it into an intervention: a technique to skip the memorizing phase Tale of Two Circuits describes, rather than just observing it. |
| [Grokking as the Transition from Lazy to Rich Training Dynamics](https://arxiv.org/abs/2310.06110) | Kumar, Bordelon, Gershman, Pehlevan | 2023 | A feature-learning / kernel-regime account of grokking, giving a theoretical (NTK-adjacent) complement to the mechanistic account. |
| [Grokking on the Weight-Decay Clock: A Rate Hierarchy from Softly Broken Symmetries](https://arxiv.org/abs/2607.23967) | Kim | 2026 | Another exactly-solvable theoretical account, complementary to the lazy-to-rich picture above: an explicit late-time relaxation mechanism tied specifically to weight decay and symmetry breaking. |
| [Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns](https://arxiv.org/abs/2606.25010) | Baherwani, Chen, Qiu, Wilson, Izmailov | 2026 | Connects grokking's small-algorithmic-task puzzle — sudden generalization — to the same abruptness seen in emergent capabilities at full LLM scale, closing out the section by scaling the whole question up. |

*Extended reading: [`extended-reading/07-training-dynamics-and-grokking.md`](extended-reading/07-training-dynamics-and-grokking.md).*

---

## 8. Scaling Interpretability & Automated Interp

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Language Models Can Explain Neurons in Language Models](https://openai.com/index/language-models-can-explain-neurons-in-language-models/) | Bills, Cammarata, Mossing, et al. (OpenAI) | 2023 | First large-scale attempt to automate feature interpretation using models to label neurons: origin of the "autointerp" pipeline now standard for SAE evaluation. |
| [Language Models Can Explain Visual Features via Steering](https://arxiv.org/abs/2603.22593) | Ferrando, Lopez-Cuena, Martin-Torres, Hinjos, Arias-Duart, et al. | 2026 | Extends autointerp from captioning to steering, and from language to vision-model SAE features — a natural next step on the pipeline the paper above started. |
| [LLMs Can Annotate Attribution Graphs](https://arxiv.org/abs/2608.02632) | Patel, Zhang, Hu | 2026 | Automates the time-intensive manual step of grouping features/neurons into supernodes for circuit tracing — applies the autointerp idea to a newer interpretability artifact than neuron labeling. |
| [Automated Attention Pattern Discovery at Scale in Large Language Models](https://arxiv.org/abs/2604.03764) | Katzy, Popescu, Mekkes, Deursen, Izadi | 2026 | States the section's core tension directly: interpretability methods haven't scaled the way capabilities have, and proposes automated attention-pattern discovery as one lever. |
| [Pitfalls in Evaluating Interpretability Agents](https://arxiv.org/abs/2603.20101) | Haklay, Prakash, Pandey, Torralba, Mueller, et al. | 2026 | A check on the automation papers above: as interpretability itself gets delegated to automated agents, this catalogs how their evaluations can be misleading. |
| [Automatically Finding Reward Model Biases](https://arxiv.org/abs/2602.15222) | Wang, Arcuschin, Conmy | 2026 | A concrete applied case of automated interpretability at work — surfacing spurious reward-model biases (length, format, sycophancy) without hand-specifying what to look for. |
| [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) | Sharkey et al. (community position paper) | 2024 | A frank list of unsolved problems: good orientation piece for picking a thesis-scale research question. |
| [Does Circuit Analysis Interpretability Scale?](https://arxiv.org/abs/2307.09458) | Lieberum et al. | 2023 | (Cross-listed from §2: belongs equally here as a scaling-limits paper.) |
| [Language Model Circuits Are Sparse in the Neuron Basis](https://arxiv.org/abs/2601.22594) | Arora, Wu, Steinhardt, Schwettmann | 2026 | A structural finding that bears directly on the scaling question above: if circuits are sparse in the neuron basis specifically, that's part of why post-hoc decomposition (SAEs, §3) has been necessary at all. |
| [Rethinking Interpretability in the Era of Large Language Models](https://arxiv.org/abs/2402.01761) | Singh, Askari, Caruana, Gao et al. | 2024 | Surveys how interpretability goals and methods shift once models are prompted/instructed rather than only probed. |

*Extended reading: [`extended-reading/08-scaling-and-automated-interp.md`](extended-reading/08-scaling-and-automated-interp.md).*

---

## 9. Applications: Safety, Steering, Unlearning

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Steering Language Models With Activation Addition](https://arxiv.org/abs/2308.10248) | Turner, Thiergart, Leech, Udell, Vazquez, Mini, MacDiarmid | 2023 | Simple, effective activation-steering technique: direct, practical downstream use of the linear representation hypothesis. |
| [Latent Fact-Checking: Detecting Misinformation through Activation Engineering](https://arxiv.org/abs/2608.06417) | Barcelos, Parraga, Mussi, Fraga, Kupssinskü, et al. | 2026 | A concrete application of activation-engineering-style techniques to a fresh, high-stakes use case (misinformation detection) rather than another steering benchmark. |
| [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) | Zou, Phan, Chen, et al. | 2023 | Proposes representation-level (rather than circuit-level) control as a tractable alternative interpretability paradigm: a useful contrast case against feature- and circuit-level approaches. |
| [RepBench: Compiling Benchmarks into Capability Representations for Large Language Models](https://arxiv.org/abs/2607.28008) | Li, Bai, Liu, Zhang | 2026 | Addresses a real gap left by the paper above: representation-engineering methods are typically evaluated on paper-specific synthetic data, making results hard to compare across papers. |
| [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) | Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda | 2024 | A clean, high-impact single-direction finding with direct safety relevance: good example of geometry-to-behavior causal claims done carefully. |
| [A Cross-Architecture Audit of Direction-Based Inference-Time Defences in Vision-Language Models](https://arxiv.org/abs/2607.27910) | Yin, Bodin, Menon, Cheng | 2026 | Directly audits whether the single-direction idea above generalizes as a *defense* mechanism (subtracting a jailbreak direction) across five candidate methods and multiple VLM architectures. |
| [Emergent Misalignment Recruits a Pre-existing Persona Subspace](https://arxiv.org/abs/2607.21356) | Nadaf | 2026 | A mechanistic account of one of the field's most consequential recent findings — that narrow fine-tuning on bad advice can broadly misalign a model — explained as recruiting a subspace that was already there. |
| [Inducing language models to assert their own consciousness restores human beliefs and values](https://arxiv.org/abs/2607.28607) | Kim, Street, Rocca, Korngiebel, Waytz, et al. | 2026 | An empirical finding about representational side effects of safety training: aligning models to deny self-consciousness measurably shifts their representations of mindedness in *other* entities too, alongside human beliefs and values. |
| [Gradient Concentration, Not Weight Saliency, Explains Representation-Level Class Unlearning](https://arxiv.org/abs/2607.21353) | Habbati, Merlo, Verderame, Guerar | 2026 | Explains *why* a class of unlearning methods works rather than proposing another one — the field's first unlearning entry earns its place by being explanatory, not just another technique. |
| [Eliciting Latent Knowledge: How to Tell if Your Eyes Deceive You](https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/) | Christiano, Cotra, Xu (ARC) | 2021 | Foundational safety-motivated problem statement: not a standard "paper" but the canonical ELK framing many interpretability agendas cite as motivation. |

*Extended reading: [`extended-reading/09-applications-safety.md`](extended-reading/09-applications-safety.md).*

---

## 10. Surveys & Reviews

Good for orientation or for writing a related-work section.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [A Survey of Mechanistic Interpretability](https://arxiv.org/abs/2407.02646) | Rai, Zhou, Feng, Saparov, Yao | 2024 | Broad, methods-organized survey: good starting map before diving into individual sections above. |
| [Explainability for Large Language Models: A Survey](https://arxiv.org/abs/2309.01029) | Zhao, Chen, Yang, Liu, Deng, Cai, Wang, Yin, Du | 2023 | Wider XAI lens (not mech-interp-specific): useful for situating mech interp among other interpretability paradigms. |
| [Mechanistic Interpretability for AI Safety: A Review](https://arxiv.org/abs/2404.14082) | Bereska & Gavves | 2024 | Safety-motivated framing of the field, complements the ELK-style motivation in §9. |

---

## 11. Tools & Libraries

| Tool | Maintainer | Purpose |
|---|---|---|
| [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) | Nanda et al. / community | The standard library for activation caching, patching, and circuit analysis on open-weight transformers. |
| [SAELens](https://github.com/jbloomAus/SAELens) | Bloom et al. | Training and analyzing sparse autoencoders on top of TransformerLens. |
| [Neuronpedia](https://www.neuronpedia.org/) | Neuronpedia team | Hosted, searchable database of SAE features across many open models (including Gemma Scope). |
| [CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis) | TransformerLens community | Interactive visualization of attention patterns and circuit-analysis artifacts. |
| [pyvene](https://github.com/stanfordnlp/pyvene) | Stanford NLP | Library for causal-abstraction-style interventions (activation/representation editing) at scale. |

---

## Suggested Reading Order (if starting from zero)

1. §1 Foundations, papers 1→4 in order (Zoom In → Circuits Framework → Toy Models of Superposition)
2. §2 Circuits & Features, IOI paper first
3. §3 Superposition & SAEs, in table order
4. §6 In-Context Learning (induction heads: pairs naturally with the Circuits Framework paper)
5. §5 Causal Methods (you'll want this toolkit before reading §4 and §7 critically)
6. §4 Representation Geometry
7. §7 Training Dynamics & Grokking
8. §8, §9 as your interests specialize
9. §10 Surveys: useful to read *after* the primary literature, to check your own map against the field's, rather than before
