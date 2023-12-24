
def run_model(device,tokenizer,
                model,context, query, **generator_args):

    input_ids = tokenizer.encode(context + "<sep>" + query, return_tensors="pt").to(device)
    res = model.generate(input_ids, **generator_args)
    output = tokenizer.batch_decode(res, skip_special_tokens=True)
    print(output)
    return output

def run(device,tokenizer,
                model ,prompt):
    query = "نظر شما به صورت کلی در مورد این خبر چیست؟"
    return run_model(device,tokenizer,
                        model ,prompt,query)