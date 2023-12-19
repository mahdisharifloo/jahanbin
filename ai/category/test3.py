from transformers import MT5Config, MT5ForConditionalGeneration, MT5Tokenizer

model_name = "persiannlp/mt5-small-parsinlu-qqp-query-paraphrasing"
tokenizer = MT5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

def run_model(q1, q2, **generator_args):
    input_ids = tokenizer.encode(f"{q1}<sep>{q2}", return_tensors="pt")
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output


# run_model("چه چیزی باعث پوکی استخوان می شود؟", "چه چیزی باعث مقاومت استخوان در برابر ضربه می شود؟")
# run_model("من دارم به این فکر میکنم چرا ساعت هفت نمیشه؟", "چرا من ساده فکر میکردم به عشقت پابندی؟")
# run_model("دعای کمیل در چه روزهایی خوانده می شود؟", "دعای جوشن کبیر در چه شبی خوانده می شود؟")
# run_model("دعای کمیل در چه روزهایی خوانده می شود؟", "دعای جوشن کبیر در چه شبی خوانده می شود؟")
# run_model("شناسنامه در چه سالی وارد ایران شد؟", "سیب زمینی در چه سالی وارد ایران شد؟")
# run_model("سیب زمینی چه زمانی وارد ایران شد؟", "سیب زمینی در چه سالی وارد ایران شد؟")


clean = 'فردا جمع بشید میدون انقلاب تا اعتراضمونو نشون بدیم'
q = 'این متن دعوت به اعتراض است'
run_model(clean,q)

print('test')