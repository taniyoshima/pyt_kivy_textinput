# pyt_kivy_textinput

<br>

## 内容

textinputのサンプルプログラム。（1行のTextInputの設定）

### テキストの表示位置を指定する

テキストの水平方向の表示位置は、プロパティhalignで指定します。
halignの値には、’auto'(デフォルトの値), 　’left’,　 ‘center’,　 ‘right’があります。  

※ 今回は、1行のテキストを使用するため、multiline: Falseを指定しています。

```
        TextInput:
            text:'テキスト１'
            halign: 'right'
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            multiline: False
```

<br>

### テキストにヒント表示を追加する

テキストのヒント表示をするには、ヒントをhint_textで指定します。また、hint_text_colorを指定することで、ヒントの色を指定することができます。

```
        TextInput:
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            hint_text:'テキスト２'
            hint_text_color: [0.0, 0.0, 1.0, 1.0]
            multiline: False
```

<br>

### テキストを数字のみを入力可能にする

TextInputへ入力可能な文字を制限するのには、プロパティinput_filterを使用します。input_filterの値には以下の3つを選択可能です。  
’int’ :　　テキストには整数が入力可能。  
’float’: 　 テキストには小数を入力可能。  
関数を指定：　次作の入力フィルタが設定可能（次で説明）

このため、テキストに数字のみを入力可能にするには、input_fileに ‘int’を指定します。

```
        TextInput:
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            hint_text:'テキスト３:数値入力'
            hint_text_color: [0.0, 1.0, 0.0, 1.0]
            input_filter: 'int'
            multiline: False
```

<br>

### テキストに自作した入力フィルタを設定する

　input_filerには自作したフィルタ（関数）を指定することが可能であり、その場合は「input_filter: root.(関数名)」と記入します。そして、pythonファイルに同じ関数名を付けた関数を作成すると、その関数に記入したルールでフィルタ処理がおこなわれます。

```
        TextInput:
            font_name: 'MPLUS1-Medium.ttf'
            font_size: '20pt'
            hint_text:'テキスト４:アルファベット入力'
            hint_text_color: [0.0, 1.0, 0.0, 1.0]
            input_filter: root.my_input_filter
            multiline: False
```

```
    def my_input_filter(self, string, bool):
        out = re.match(r'[a-zA-Z0-9.!#$%&@]', string)
        if out is None:
            return ''
        else:
            return out.group()
```

<br>

## 参考にしたHP
