<script lang="ts">
    import {Alert,Accordion } from '@svelteuidev/core';
    import {Hand, InfoCircled} from 'radix-icons-svelte';
    import data from "./result.json"
    import {Input, InputWrapper} from '@svelteuidev/core';

    let answerData = []
    let question = ""


    function debounce(func, delay) {
        let timer = null;
        return function (...args) {
            if (timer) clearTimeout(timer);
            timer = setTimeout(() => {
                func.apply(this, args);
            }, delay)
        }
    }

    const submit = debounce(() => {
        answerData = []
        for (const key in data) {
            if (key.includes(question)) {
                answerData.push({
                    'q': key,
                    'a': data[key]
                })
            }
        }
        answerData = answerData
    }, 1000)

</script>

<main>
    <Alert icon={InfoCircled} title="注意!" color="blue">
        本网站免费开放，不会主动收取费用
        <a href="https://jcdn.lawliet.ren/qrcode.jpg" target="_blank" class="font-bold underline">加入微信群</a>
    </Alert>
    <div class="mt-4">
        <Input icon={Hand}
               on:keyup={submit}
               bind:value={question}
               placeholder="请输入你的问题"
               radius="xs"
        />
    </div>
    <Accordion radius="xs">
        {#each answerData as answer}
            <!--{answer.q.substring(1,10)}-->
            <Accordion.Item>
                <div slot="control">Question : {answer.q}</div>
                <div class="font-bold">Answer : {answer.a}</div>
            </Accordion.Item>
        {/each}
    </Accordion>
</main>

<style>
</style>
