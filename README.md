<html>
   <h2>About the project</h2>
     <h4> I built a Movie Search Engine by fine-tuning the BERT model on Bing queries and Quora question triplets.</h4>
     <h3>Search Engine</h3>
     <h4>I implemented BERT using PyTorch and Hugging Face transformers library. I used BERT Small with 6 layers and 10 attention heads petrained by Google.
     I fine-tuned two models for symmetric and asymmetric search engines. The fine-tuning pipeline for both algorithms consisted of filtering data and fine-tuning model
     using unsupervised approach, i.e Multi-negative ranking Loss with hard negatives. For assymetric model I used a sample from MsMarco tripletes
     dataset (Bing queries) and for symmetic model I used Quora question/answer Triplets. Both datasets are available at <a href="https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/paraphrases/">Paraphrase Data.</h3>
     <h3>Movies Dataset and Indexing</h3>
     <h4>I implemeted th search engine on a IMDB Movie dataset by building a Movie recommender. I used Annoy library to index movie plots to speed up the search process.<h4>
     <h3>Autocomplete</h3>
     <h4>I implemented an autocomplete in my Search Engine by builing a Trie pefix tree from scratch using movie titles. The autocomplete algorithm is not case sensitive.</h4>
  <h2>Repository Structure</h2>
      <h3>Collecting Data and Notebooks</h3>
      <h4>The ML branch containes fine-tuning data and ipython notebook with the training process</h4>
      <h3>Django project</h3>
      <h4>The master branch contains a Django project
<html>
