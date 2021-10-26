sum_fibonacci = 2

fn_2 = 1
fn_1 = 2
fn_0 = (fn_2 + fn_1)

while fn_0 < 4000000:
    fn_0 = fn_1+fn_2
    if (fn_0 % 2 == 0):
        sum_fibonacci += fn_0
    fn_2 = fn_1
    fn_1 = fn_0

print(sum_fibonacci)