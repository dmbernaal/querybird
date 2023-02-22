Querybird is a lightweight API used to summarize and ask any questions on uploaded/linked text. This app is a great way for make large corpuses of text interactive. For instance, a student may be studying for biology and wants to test themselves on the subject matter on a given chapter. They may upload the chapter text onto our platform and then ask questions against it. 

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
