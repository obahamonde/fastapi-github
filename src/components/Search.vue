<script setup lang="ts">
  import { ComputedRef, Ref } from 'vue';
  const search = ref("")
  const results = ref([]) as Ref<any[]>
  const page = ref(0)
  const lang = ref('en-US')
  const speech = useSpeechRecognition({
    lang,
    continuous: true,
  })
  const SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
  const speechRecognitionList = new SpeechGrammarList()
  speechRecognitionList.addFromString(1)
  speech.recognition!.grammars = speechRecognitionList
  
  const toggle = ref(false)
  const { isListening, stop, result } = speech
  const selectedLanguage = ref(lang.value)
  watch(lang, lang => selectedLanguage.value = lang)
  watch(isListening, isListening => isListening ? null : selectedLanguage.value = lang.value)
  watchEffect(() => search.value ? null : results.value = [])
  const start = () => {
    search.value = "..."
    speech.start()
  }
  const query: ComputedRef<string | undefined> = computed(() => {
    if (!isListening.value) {
      return search.value.length > 0 ? search.value.split(" ").join("+") : "";
    }
    else if (isListening) {
      return result.value.split(" ").join("+")
    }
  
  })
  
  function handleToggle() {
    toggle.value = !toggle.value
    results.value = []
    search.value = ""
  }
  
  function searchQueryspeech() {
  
    const { data } = useFetch(`https://dstzf5kmgfl76io5ynsn3yn7hm0gbeur.lambda-url.us-east-1.on.aws/${unref(lang)}/${unref(query)}/${unref(page)}`).json()
    results.value = data
    stop()
  }
  
  function searchQuery() {
  
    const { data } = useFetch(`https://dstzf5kmgfl76io5ynsn3yn7hm0gbeur.lambda-url.us-east-1.on.aws/${unref(lang)}/${unref(query)}/${unref(page)}`).json()
    results.value = data
  
  }
  
  function nextPage() {
    page.value += 1
    searchQuery()
  }
  
  function prevPage() {
    page.value -= 1
    searchQuery()
  }
  
  function toSpanish() {
    lang.value = "es"
    page.value = 0
    searchQuery()
  }
  
  function toEnglish() {
    lang.value = "en"
    page.value = 0
    searchQuery()
  }
  
  function toFrench() {
    lang.value = "fr"
    page.value = 0
    searchQuery()
  }
  
  </script>
    <template>
    <div col :class="!toggle ? 'bg-gray-500 p-2 rf tr fixed m-4 mt-4':'shadow-lg shadow-gray-500 rounded-xl max-w-58 m-auto p-1'">
      <div col center w-auto >
        <div row center border-gray-500 b-2 rounded-xl hover-bg-transparent  >
          <div i-carbon-search   cp scale @click.prevent="handleToggle" :class="!toggle ? 'text-white p-2 rf':'text-secondary'"  />
          <h1 row v-if="toggle" fade-in-left><input type="search" bg-transparent no-outline  text-secondary dark:text-primary v-model="search"
              @keyup.enter="searchQuery" @keyup.escape="handleToggle" />
              <span row center>
            <Ico icon="mdi-microphone" text-xl text-secondary cp dark:text-primary v-if="!isListening"
              @click="start" />
            <Ico icon="mdi-microphone-off" text-xl text-secondary cp dark:text-primary v-else
              @click="searchQueryspeech" />
            </span></h1>
        </div>
      </div>
      <div row center pb-2 v-if="search" fade-in-down mt-2> <label :id="lang" class="radio">
          <input v-model="lang" value="en" type="radio" hidden>
          <img src="/images/us.svg" mx-1 cp scale @click="toEnglish"
            :class="{ 'shadow-black scale-125 dark:shadow-white shadow-md': lang === 'en' }" />
  
          <span>
          </span>
        </label>
        <label :id="lang" class="radio">
          <input v-model="lang" value="fr" type="radio" hidden>
          <img src="/images/fr.svg" mx-1 cp scale @click="toFrench"
            :class="{ 'shadow-black scale-125 dark:shadow-white shadow-md': lang === 'fr' }" />
  
        </label>
        <label :id="lang" class="radio">
          <input v-model="lang" value="es" type="radio" hidden>
          <img src="/images/pe.svg" mx-1 cp scale @click="toSpanish"
            :class="{ 'shadow-black scale-125 dark:shadow-white shadow-md': lang === 'es' }">
  
        </label>
      </div>
      <div v-if="search">
        <div v-for="r in unref(results)" col >
          <a :href="r.url" text-xs underline m-2 hover:text-primary>{{ r.title }}</a>
        </div>
        <div row center mt-6 v-if="(unref(results).length > 0)">
          <Ico icon="mdi-chevron-left" text-xl mx-1 text-secondary cp dark:text-primary v-if="page > 0"
            @click="prevPage" />
          {{ page + 1 }}
          <Ico icon="mdi-chevron-right" text-xl mx-1 text-secondary cp dark:text-primary v-if="page < 10"
            @click="nextPage" />
        </div>
      </div>
    </div>
  </template>
