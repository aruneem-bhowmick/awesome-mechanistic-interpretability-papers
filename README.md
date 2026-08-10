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
| [Identifying Functionally Important Features with End-to-End Sparse Dictionary Learning](https://arxiv.org/abs/2405.12241) | Braun, Bushnaq, Heimersheim, Mendel, Sharkey | 2024 | Directly relevant to identifiability: asks whether SAE features are the *right* decomposition rather than just *a* sparse one. |

---

## 4. Representation Geometry & Linear Structure

The geometric/representational lens: how models encode information in the structure of activation space, as opposed to in discrete circuits.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Linear Algebraic Structure of Word Senses, with Applications to Polysemy](https://arxiv.org/abs/1601.03764) | Arora, Li, Liang, Ma, Risteski | 2018 | Early evidence for linear/additive structure in embeddings; precursor to the modern linear representation hypothesis. |
| [The Linear Representation Hypothesis and the Geometry of Large Language Models](https://arxiv.org/abs/2311.03658) | Park, Choe, Veitch | 2023 | Formalizes the linear representation hypothesis with a causal inner product; the clearest modern statement of the hypothesis in the current literature. |
| [Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task](https://arxiv.org/abs/2210.13382) | Li, Hopkins, Bau, Viégas, Pfister, Wattenberg | 2023 | Othello-GPT: clean evidence that transformers build structured, non-linguistic world models (board state) internally. |
| [Language Models Represent Space and Time](https://arxiv.org/abs/2310.02207) | Gurnee & Tegmark | 2023 | Linear probes recover literal spatiotemporal coordinates from LLM activations: geometry as a window onto world models. |
| [The Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987) | Huh, Cheung, Wang, Isola | 2024 | Argues independently trained models converge toward a shared representational geometry as scale increases: core reading for representational convergence research. |
| [Not All Language Model Features Are Linear](https://arxiv.org/abs/2405.14860) | Engels, Michaud, Liao, Gurnee, Tegmark | 2024 | Direct challenge to the linear representation hypothesis: finds circular/multi-dimensional features (e.g., day-of-week). Essential counterpoint to Park et al. |
| Geometry of Neural Network Loss Surfaces and Representations (survey-style framing, various authors; see Sec. 10) | N/A | N/A | See Surveys section for consolidated treatment. |

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

---

## 6. In-Context Learning & Attention Circuits

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | Olsson, Elhage, Nanda, Joseph, et al. (Anthropic) | 2022 | Identifies induction heads as a specific, mechanistically understood circuit responsible for a large fraction of in-context learning. |
| [What Learning Algorithm Is In-Context Learning? Investigations with Linear Models](https://arxiv.org/abs/2211.15661) | Akyürek, Schuurmans, Andreas, Ma, Zhou | 2023 | Frames ICL as implicit gradient descent / algorithm selection: connects circuits work to a computational-mechanism hypothesis. |
| [Transformers Learn In-Context by Gradient Descent](https://arxiv.org/abs/2212.07677) | von Oswald et al. | 2023 | Constructive proof that transformers *can* implement gradient descent in a forward pass; complements Akyürek et al.'s empirical framing. |
| [Function Vectors in Large Language Models](https://arxiv.org/abs/2310.15213) | Todd, Li, Sharma, Mueller, Wallace, Bau | 2024 | Shows ICL tasks are often represented as a single steerable "function vector" in the residual stream: a geometric, not just circuit, account of ICL. |

---

## 7. Training Dynamics & Grokking

Covers how and when structured, generalizing computation emerges over the course of training, rather than only at convergence.

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets](https://arxiv.org/abs/2201.02177) | Power, Burda, Edwards, Babuschkin, Sutskever | 2022 | The original empirical discovery: sudden generalization long after training-set memorization. Sets up the puzzle. |
| [Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217) | Nanda, Chan, Lieberum, Smith, Steinhardt | 2023 | (Cross-listed from §2.) Explains grokking mechanistically as gradual circuit formation masked by loss plateaus: essential bridge between geometry, circuits, and training dynamics. |
| [Omnigrok: Grokking Beyond Algorithmic Data](https://arxiv.org/abs/2210.01117) | Liu, Michaud, Tegmark | 2023 | Extends grokking to non-algorithmic tasks and gives a weight-norm-based explanation, broadening the phenomenon beyond toy settings. |
| [The Slingshot Mechanism: An Empirical Study of Adaptive Optimizer Training Dynamics](https://arxiv.org/abs/2206.04817) | Thilak, Litwin, Shao, Rabbani, Advani, Susskind | 2022 | Ties grokking-adjacent phenomena to optimizer instabilities: a training-dynamics-first (rather than representation-first) account worth contrasting with Nanda et al. |
| [A Tale of Two Circuits: Grokking as Competition of Sparse and Dense Subnetworks](https://arxiv.org/abs/2303.11873) | Merrill, Tsilivis, Shukla | 2023 | Frames grokking as competition between a memorizing dense subnetwork and a generalizing sparse subnetwork: a useful lens for judging when a model has actually converged on a generalizing solution. |
| [Grokking as the Transition from Lazy to Rich Training Dynamics](https://arxiv.org/abs/2310.06110) | Kumar, Bordelon, Gershman, Pehlevan | 2023 | A feature-learning / kernel-regime account of grokking, giving a theoretical (NTK-adjacent) complement to the mechanistic account. |

---

## 8. Scaling Interpretability & Automated Interp

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Language Models Can Explain Neurons in Language Models](https://openai.com/index/language-models-can-explain-neurons-in-language-models/) | Bills, Cammarata, Mossing, et al. (OpenAI) | 2023 | First large-scale attempt to automate feature interpretation using models to label neurons: origin of the "autointerp" pipeline now standard for SAE evaluation. |
| [Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496) | Sharkey et al. (community position paper) | 2024 | A frank list of unsolved problems: good orientation piece for picking a thesis-scale research question. |
| [Does Circuit Analysis Interpretability Scale?](https://arxiv.org/abs/2307.09458) | Lieberum et al. | 2023 | (Cross-listed from §2: belongs equally here as a scaling-limits paper.) |
| [Rethinking Interpretability in the Era of Large Language Models](https://arxiv.org/abs/2402.01761) | Singh, Askari, Caruana, Gao et al. | 2024 | Surveys how interpretability goals and methods shift once models are prompted/instructed rather than only probed. |

---

## 9. Applications: Safety, Steering, Unlearning

| Paper | Authors | Year | Why it matters |
|---|---|---|---|
| [Steering Language Models With Activation Addition](https://arxiv.org/abs/2308.10248) | Turner, Thiergart, Leech, Udell, Vazquez, Mini, MacDiarmid | 2023 | Simple, effective activation-steering technique: direct, practical downstream use of the linear representation hypothesis. |
| [Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405) | Zou, Phan, Chen, et al. | 2023 | Proposes representation-level (rather than circuit-level) control as a tractable alternative interpretability paradigm: a useful contrast case against feature- and circuit-level approaches. |
| [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) | Arditi, Obeso, Syed, Paleka, Panickssery, Gurnee, Nanda | 2024 | A clean, high-impact single-direction finding with direct safety relevance: good example of geometry-to-behavior causal claims done carefully. |
| [Eliciting Latent Knowledge: How to Tell if Your Eyes Deceive You](https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/) | Christiano, Cotra, Xu (ARC) | 2021 | Foundational safety-motivated problem statement: not a standard "paper" but the canonical ELK framing many interpretability agendas cite as motivation. |

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
