#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_STRING_LENGTH 1000
#define MAX_SUBSTRINGS 100
int is_latin_digit_or_space(char c) {
    return (isalnum(c) || c == ' ');
}
void extract_substrings(char *str, char **substrings, int *substrings_count) {
    int i = 0, j = 0;
    *substrings_count = 0;

    while (str[i] != '\0') {
        if (is_latin_digit_or_space(str[i])) {
            substrings[*substrings_count][j++] = str[i];
        } else {
            if (j > 0) {
                substrings[*substrings_count][j] = '\0';
                (*substrings_count)++;
                j = 0;
            }
        }
        i++;
    }

    if (j > 0) {
        substrings[*substrings_count][j] = '\0';
        (*substrings_count)++;
    }
}
char* find_substring_with_max_digits(char **substrings, int substrings_count) {
    char *max_digits_substring = NULL;
    int max_digits_count = 0;

    for (int i = 0; i < substrings_count; i++) {
        int digit_count = 0;
        for (int j = 0; substrings[i][j] != '\0'; j++) {
            if (isdigit(substrings[i][j])) {
                digit_count++;
            }
        }

        if (digit_count > max_digits_count) {
            max_digits_count = digit_count;
            max_digits_substring = substrings[i];
        }
    }

    return max_digits_substring;
}
void transform_string(char *str) {
    int len = strlen(str);
    int new_len = len;

    for (int i = 0; i < len; i++) {
        if (str[i] == '1') {
            new_len++;
        }
    }

    char *new_str = (char*)malloc((new_len + 1) * sizeof(char));
    int j = 0;

    for (int i = 0; i < len; i++) {
        new_str[j++] = str[i];
        if (str[i] == '1') {
            new_str[j++] = '0';
        }
    }

    new_str[j] = '\0';
    strcpy(str, new_str);
    free(new_str);
}

int main() {
    int k;
    printf("Введите количество строк: ");
    scanf("%d", &k);
    getchar();

    if (k <= 0) {
        printf("Неверный ввод данных\n");
        return 1;
    }

    char **strings = (char**)malloc(k * sizeof(char*));
    for (int i = 0; i < k; i++) {
        strings[i] = (char*)malloc(MAX_STRING_LENGTH * sizeof(char));
        printf("Введите строку %d: ", i + 1);
        fgets(strings[i], MAX_STRING_LENGTH, stdin);
        strings[i][strcspn(strings[i], "\n")] = '\0'; 
    }

    for (int i = 0; i < k; i++) {
        char **substrings = (char**)malloc(MAX_SUBSTRINGS * sizeof(char*));
        for (int j = 0; j < MAX_SUBSTRINGS; j++) {
            substrings[j] = (char*)malloc(MAX_STRING_LENGTH * sizeof(char));
        }

        int substrings_count;
        extract_substrings(strings[i], substrings, &substrings_count);

        printf("Подстроки для строки %d:\n", i + 1);
        for (int j = 0; j < substrings_count; j++) {
            printf("%s\n", substrings[j]);
        }

        char *max_digits_substring = find_substring_with_max_digits(substrings, substrings_count);
        if (max_digits_substring) {
            printf("Подстрока с наибольшим числом цифр: %s\n", max_digits_substring);
            transform_string(strings[i]);
            printf("Преобразованная строка: %s\n", strings[i]);
        } else {
            printf("Нет подстрок, содержащих цифры.\n");
        }

        for (int j = 0; j < MAX_SUBSTRINGS; j++) {
            free(substrings[j]);
        }
        free(substrings);
    }

    for (int i = 0; i < k; i++) {
        free(strings[i]);
    }
    free(strings);

    return 0;
}
