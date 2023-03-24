Querybird is a gpt-powered audio->action application. For instance, this application can serve as a project manager who assigns product features or bug fixes to programmers - writing and submitting tickets automatically from a meeting.

## 1. Install querybird (devs only)

```
git clone https://github.com/dmbernaal/querybird.git
cd querybird
```

## 2. Install pytorch (devs only)

We use pytorch to perform internal functions such as cosine similarities for document chunk indexing and much more. We will also use pytorch to experiment and use internal language models.
You should follow proper instructions to install PyTorch via their website suitable to your machine.
[PyTorch site]("https://pytorch.org/get-started/locally/")

## 3. Install dependencies (devs only)

```
pip install -r requirements.txt
```

## 4. Start uvicorn server

```
uvicorn src.querybird.main:app --reload
```
