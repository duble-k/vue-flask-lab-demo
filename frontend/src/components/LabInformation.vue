<template>
  <div>
    <!-- Name and Image -->
    <h3>{{ result.name }}</h3>
    <v-divider></v-divider>
    <div class="text-center mb-4">
      <v-img v-if="result.image" :src="result.image" alt="Lab Image" style="max-width: 100%; max-height: 200px;"></v-img>
    </div>

    <!-- Details split into two columns -->
    <v-row>
      <!-- Left Column -->
      <v-col cols="6">
        <template v-if="result.testingSite">
          <v-row>
              <span style="color: black;">Testing Site:</span>
              <span style="color: grey;">{{ result.testingSite }}</span>
          </v-row>
        </template>

        <!-- Add other details in a similar way -->

        <!-- Example: Ordering Instructions -->
        <template v-if="result.orderingInstructions">
          <v-row>
              <span style="color: black;">Ordering Instructions:</span>
              <span style="color: grey;">{{ result.orderingInstructions }}</span>
          </v-row>
        </template>

        <template v-if="result.container">
          <v-row>
              <span style="color: black;">Container: </span>
              <span style="color: grey;">{{ result.container }}</span>
          </v-row>
        </template>

        <template v-if="result.frequency">
          <v-row>
            <span style="color: black;">Frequency:</span>
            <span style="color: grey;">{{ result.frequency }}</span>
          </v-row>
        </template>

        <template v-if="result.TAT">
          <v-row>
            <span style="color: black;">TAT:</span>
            <span style="color: grey;">{{ result.TAT }}</span>
          </v-row>
        </template>

        <template v-if="result.stabilityForAddOn">
          <v-row>
            <span style="color: black;">Stability For Add-On:</span>
            <span style="color: grey;">{{ result.stabilityForAddOn }}</span>
          </v-row>
        </template>
      </v-col>

      <!-- Right Column -->
      <v-col cols="6">
        <template v-if="result.collectionInstructions">
        <v-row>
          <span style="color: black;">Collection Instructions:</span>
          <span style="color: grey;">{{ result.collectionInstructions }}</span>
        </v-row>
        </template>
        <!-- Add other details in a similar way -->

        <!-- Example: External Link -->
        <template v-if="result.externalLink">
          <v-row>
            <span style="color: black;">For all other information:</span>
            <a :href="result.externalLink" target="_blank" rel="noopener noreferrer" style="color: blue; cursor: pointer; word-wrap: break-word;">
              {{ result.externalLink }}
            </a>
          </v-row>
        </template>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  props: {
    result: Object, // Assuming 'result' is an object passed as a prop
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
