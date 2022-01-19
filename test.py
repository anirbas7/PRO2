import time
time.strftime('%Y-%m-%d %H:%M', time.localtime())
print(time.strftime('%Y-%m-%d %H:%M'))
datensatz(
    sFormat := '%4u.%2u.%2u;%2u:%2u;%2u-%1u;',
    arg1 := (time.strftime('%Y')),
    arg2 := F_WORD(time.strftime('%m')),
    arg3 := F_WORD(time.strftime('%d')),
    arg4 := F_WORD(time.strftime('%H')),
    arg5 := F_WORD(time.strftime('%M')),
    arg6 := F_WORD(name),
    arg6 := F_WORD(zahl),
    bError= >,
nErrId = >,
sOut = > s_Datensatz_a);
