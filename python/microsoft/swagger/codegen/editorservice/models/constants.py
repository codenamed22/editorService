from python.microsoft.swagger.codegen.editorservice.models import descriptor

desc1 = descriptor.Descriptor("LicenseType", "Subscription")
desc2 = descriptor.Descriptor("IsCompliant", "true")
desc3 = descriptor.Descriptor("FlightIDs", "Wac-WordEditorServiceMultipleGrammarCritiquesPerSentence-Treatment")

listDes = [desc1, desc2, desc3]
listIncludedCrit = ["Spelling", "Grammar", "Conciseness", "Vocabulary"]
listCritWeight = [1, 0.5, 0.25, 0.2]
language = "en-us"
profileId = "99000000-0000-0000-0000-000000000000"
text_unit = "Sentence"
appId = "Word_Online"