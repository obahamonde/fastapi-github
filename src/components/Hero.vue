<template>
    <div col center>
        <h1 m-2 font-script text-4xl text-warning>{{props.brand}}</h1>
        <img :src="props.logo" alt="logo" width="100" dark:invert animate-rotate-in />
        <section m-8 text-2xl font-script text-success >
            <h1 my-4 text-shadow-xl shadow-gray-500>
                {{ props.cta}}
            </h1>
            <h2 my-4 text-shadow-xl shadow-gray-500>
                {{ props.slug }}
            </h2>
            <button btn-post font-sans rounded-lg m-8 @click="start()">Get Started</button>
        </section>
       
        <GetStarted z-50 tl fixed h-screen w-screen v-if="toggle" />
       
    </div>
</template>
 
<script setup lang="ts">
const props = defineProps<{
    cta: string
    slug: string
    brand: string
    logo: string
}>()

const toggle = ref(false)
const start = async() => {
    toggle.value = true
    setTimeout(() => {
        toggle.value = false
       
    }, 3000)
    setTimeout(() => {
    }, 2500)
}

</script>
