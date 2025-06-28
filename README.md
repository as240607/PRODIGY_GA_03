## 📚 Task-03: Text Generation with Markov Chains

### 📝 Objective

This task focuses on implementing a simple **text generation algorithm using Markov Chains**. The core idea is to train a probabilistic model that learns how often certain characters or words follow each other and then uses that statistical knowledge to generate new, coherent sequences that mimic the style of the input text.

---

### ⚙️ Technologies & Tools Used

* **Python**
* **markovify**: A Python library used for building Markov models for text generation.
* **collections.Counter**: For word/character frequency analysis.
* **random**: For sampling and randomness.
* **JSON**: For optional external data input.

---

### 🔍 Features

* **Loads and processes two text sources**:

  * `1342-0.txt` (e.g., *Pride and Prejudice* by Jane Austen)
  * `84-0.txt` (e.g., *Frankenstein* by Mary Shelley)

* **Displays basic statistics**:

  * Top characters and words using `collections.Counter`.
  * Random word samples from each text.

* **Word-level Markov Chain Generation**:

  * Uses `markovify.Text` to build models.
  * Generates full and short sentences.
  * Supports different *state sizes* (e.g., 1 for unigram, 4 for 4-gram-like structures).

* **Character-level Markov Chain Generation**:

  * Custom class `SentencesByChar` overrides the default behavior of `markovify.Text` to operate at the character level instead of the word level.
  * Demonstrates how a sentence can be generated letter by letter.

* **Model Combination**:

  * Combines two models (e.g., Austen and Shelley) using weighted blending (e.g., 50-50).

* **Flexible Configuration**:

  * Easily switch between word-level and character-level generation.
  * Customizable output length, number of outputs, and Markov order.

* **Optional Features**:

  * If available, reads and generates:

    * Line-wise Shakespearean sonnets from `sonnets.txt`
    * Mood-based phrases from `moods.json`

---

### 🚀 How It Works

1. **Text Input & Cleaning**:
   The script reads two classic literary texts and splits them into word and character sequences.

2. **Model Building**:
   It builds multiple types of Markov models using:

   * Word-level transitions
   * Character-level transitions (via subclassing)

3. **Generation Examples**:
   Generates text samples with different configurations:

   * Sentence length limits
   * Output count
   * N-gram state size (e.g., 1 to 7)

4. **Blending Models**:
   It merges the styles of the two texts using `markovify.combine`, producing hybrid-generated text.

5. **Optional Data Support**:

   * Shakespeare sonnets and mood phrases are used if their respective files are available.

---

### 📂 Output Examples

Depending on configuration, output may look like:

**Word-level output:**

> “The family of Eliza had often led him to the door.”

**Character-level output:**

> “We hroulded to me bere we sed and be all.”

**Combined style:**

> “Her soul overflowed with warmth as the storm approached.”

---

### 📌 References

* [Markov Chains](https://en.wikipedia.org/wiki/Markov_chain)
* [markovify GitHub Repo](https://github.com/jsvine/markovify)
* [Project Gutenberg (for text sources)](https://www.gutenberg.org/)
