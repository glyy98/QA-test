1、主机=cpu+主存储器
2、中央处理单元（CPU）=  运算器、控制器、寄存器组、内部总线
3、运算器的组成：
算数逻辑单元ALU（实现对数据的算术和逻辑运算）
累加寄存器AC（运算结果或源操作数的存放区）
数据缓冲寄存器DR（暂时存放内存的指令或数据）
状态条件寄存器PSW（保存指令运行结果的条件码内容：溢出标志）

运算器功能：执行所有的算术运算、逻辑运算
4、控制器的组成：
指令寄存器IR（暂存cpu执行指令）
程序计数器PC（存放指令执行地址）
地址寄存器AR（保存当前cpu所访问的内存地址）
指令译码器ID（分析指令操作码）

控制器功能：很重要！控制整个cpu的工作，程序控制、时序控制

5、进制转化


6、机器数
无符号代表正数

带符号数的最高位是符号位
正数是0  负数是1

真值：机器数对应的实际数值（10进制）

7、数据表示（计算机默认按8位编制）
例如：当真值为-45

原码：-0和+0
真值的二进制 

负数为1  45的二进制：101101  只有6位，前面要补个0，变成7位
最高位是符号位+7位
10101101

反码：-0和+0
1、正数的反码=正数的原码
2、负数：符号位不变，其他各位按位取反

补码：只有+0
1、正数的补码=正数的原码
2、负数：除符号位，其他各位按位取反后+1，如果7位需要进位，符号位会发生改变

移码：只有+0
将原码的补码的首位取反，正数负数都是要运算


8、码制范围
原码和反码，少一个位，所以需要-1

A=2^(n-1)  取特殊值 n=3  
两位的二进制数可以表达几个  4个数 00 01 10 11
表示的范围是0 1 2 3  0-3 
因为是从0开始编号，所以要减1

定点整数：原码和反码范围一样，补码和移码范围一样
原码：-（A-1) ~  +（A-1)
反码：-（A-1) ~  +（A-1)
补码：-A ~ + （A-1）  因为只有+0，所以只用在+0去减1
移码：-A ~ + （A-1)   

定点小数：把整数部分，整体除于2^（n-1）
动手算一下就知道了，负数~正数


9、浮点数
N=F*2^E  E是阶码，确定数值范围
F是尾数，确定数值精度

例如:二进制，101.011= 0.101011 * 2^ 3
                       尾数F       阶码E   
阶符 阶码 数符 尾数

10、浮点数的运算
先对阶，小阶向大阶看齐，尾数缩小，会丢失末位，影响不大
如果是大阶对齐小阶，会丢失高位，精度会大变化，不可行
运算完规格化：符号尾数的补码，负数表示：1.0xxxx  正数表示：0.1xxxx

真题运算：
2x的补码是90H，那么x的真值是什么
思路：90H 换成二进制：1001 0000
符号位 1  负数 ，负数的补码转为原码需要计算
原码-补码，符号位不变，各位取反+1
补码-原码，-1后各位取反
得出：1,111 0000  是原码
二进制转为十进制  - 112
2x=-112  x为-56

真题运算：
设16位浮点数，阶符1位，阶码值6位，数符1位，尾数8位。
若阶码用移码表示，尾数用补码表示，则浮点数所能表示的数值范围是
 
思路：指数最大是2^6=64 但如果表达范围要-1 64-1=63
根据公式：F*2^E
所以是2^63
F是尾数，用补码表示，先写出整数的，再整体除于2^(n-1)
-1~ + 1-2^-(n-1) 这里的n要代入9  n是包括符号的8+1=9
F=-1~ + [1-2^(-8)] * 2^63
-2^63 ~ + [1-2^(-8)] * 2^63
