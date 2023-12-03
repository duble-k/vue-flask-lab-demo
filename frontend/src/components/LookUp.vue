<template>
  <v-container fluid>
    <v-row justify="center" align="center" class="pb-4">
      <!-- Autocomplete search input -->
      <v-col cols="9">
        <v-autocomplete
          v-model="searchInput"
          :items="names"
          label="Search Lab Item"
          outlined
          @keydown.enter="handleAutocompleteKeyDown"
        ></v-autocomplete>
      </v-col>
      <!-- Search button -->
      <v-col cols="2">
        <v-btn @click="handleSearch" outlined>
          Search
        </v-btn>
      </v-col>
      <!-- Loading spinner -->
    <v-col cols="1">
    <template v-if="isLoading">
        <v-progress-circular indeterminate size="20" class="ml-2"></v-progress-circular>
    </template>
    </v-col>
    </v-row>
    <template v-if="result">
      <v-card elevation="3" class="p-3 mt-3">
        <v-tabs v-model="tabValue" align-tabs="center">
          <v-tab @click="tabValue=0">
            <v-icon>mdi-information</v-icon>
            Information
          </v-tab>
          <v-tab @click="tabValue=1">
            <v-icon>mdi-file-document</v-icon>
            Forms
          </v-tab>
        </v-tabs>
        <v-container p="3">
          <!-- Lab Information component -->
          <LabInformation v-if="tabValue === 0" :result="result" />
          <!-- Forms List component -->
          <FormsList
            v-if="tabValue === 1"
            :name="result.name"
            :associated-pdfs="result.associatedPdfs"
          />
        </v-container>
      </v-card>
    </template>
  </v-container>
</template>

<script>
import LabInformation from "@/components/LabInformation.vue";
import FormsList from "@/components/FormsList.vue";
import { ref, reactive, onMounted } from "vue";
import fetchNames from "@/api/fetchNames";
import fetchInfo from "@/api/fetchInfo";

export default {
  components: {
    LabInformation,
    FormsList,
  },
  setup() {
    const searchInput = ref(null);
    const names = ref([]);
    const result = ref(null);
    const tabValue = ref(0);
    const isLoading = ref(false);

    const handleSearch = async () => {
      if (!names.value.includes(searchInput.value)) {
        open.value = true;
        message.value = "Invalid search input. Please select a valid option from the list.";
        severity.value = "warning";
        return;
      }

      isLoading.value = true;
      try {
        const resultData = await fetchInfo({ name: searchInput.value });
        result.value = resultData;
      } catch (error) {
        // Handle error
      } finally {
        isLoading.value = false;
      }
    };

    const handleAutocompleteKeyDown = (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        handleSearch();
      }
    };

    onMounted(async () => {
      names.value = await fetchNames();
      console.log(names.value);
    });

    return {
      searchInput,
      names,
      result,
      tabValue,
      isLoading,
      handleSearch,
      handleAutocompleteKeyDown,
    };
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
