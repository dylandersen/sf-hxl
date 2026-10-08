# Agentforce output widgets

HXL explicitly lists Agentforce Employee agent in Lightning Experience. Broader CLT/LWC mobile and Enhanced Chat support does not establish HXL support there.

## Data and renderer

Use structured action output and one Apex-backed CLT for the documented HXL Agentforce pattern. Actions may be backed by Apex, Flow, Prompt Template, or another supported asset; match the CLT to the actual output structure. A plain string output does not become a structured widget automatically.

```text
lightningTypes/accountSummaryResponse/
  schema.json
  renderer.json
```

Schema:

```json
{
  "title": "Account summary response",
  "lightning:type": "@apexClassType/c__AccountSummaryResponse"
}
```

Renderer:

```json
{
  "renderer": {
    "componentOverrides": {
      "$": {
        "definition": "@widget/c/accountSummary",
        "attributes": {
          "name": "{!$attrs.name}",
          "annualRevenue": "{!$attrs.annualRevenue}"
        }
      }
    }
  }
}
```

Store the renderer beside the schema. HXL references in `editor.json` or LWC channel subdirectories are unsupported. Mapping keys exist in the widget schema; mapping values name actual output fields.

## New Apex data types

The dedicated Apex CLT guide requires separate top-level `global` classes, `@JsonAccess(serializable='always' deserializable='always')` on each class, and `@AuraEnabled` on every projected response field, including fields inside invocable objects. Add appropriate invocable annotations to invocable variables. Preserve sharing and CRUD/FLS enforcement in business logic; rendering does not replace Apex data access controls.

Supported projection includes primitives, sObjects, lists/arrays, string-keyed maps, and user-defined classes. The CLT schema points at the class rather than duplicating its projected properties. HXL hotel samples use inner-class references, while the dedicated Apex guide instructs new types to use top-level classes. Follow dedicated requirements for new work and validate sample references against the target org. See [inconsistencies](troubleshooting.md#documentation-inconsistencies).

Adding exposed fields is additive. Renaming/deleting referenced classes, removing output fields, changing field types, or downgrading visibility may break active actions. If an action was registered before required annotations existed, the guide instructs recreating it after fixing the classes; do that only within the user's requested scope.

## Configure output rendering

Deploy Apex and widget/CLT metadata first. Attach the action to a subagent and the subagent to the target agent. Descriptions/reasoning should distinguish the task, select the action, and collect missing inputs.

In Setup **Agentforce Assets → Actions**, open the action, edit its structured output, select **Show in conversation**, and select the deployed CLT in **Output Rendering**. Save and reload the agent page. Match the output's actual data type, not just a similar label.

Exercise the same request before and after custom rendering. Verify subagent routing, action invocation, structured data, and displayed field values. Deployment alone does not establish these runtime stages.

## Follow-up buttons

Use `action/sendMessage` with enough identifying context for the record/task. Make the follow-up business action available to the subagent and configure its reasoning. The hotel example uses reservation/cancellation, but those are examples, not mandatory features. Check that selecting a button sends the intended message and chooses the correct action. See [button](components/button.md) and [interactions](type-contracts.md#interactions).

Sources: [action output](https://developer.salesforce.com/docs/platform/hxl/guide/agentforce-action-output.html), [mapping](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping.html), [Apex CLTs](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-apex.html), [core CLTs](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-core.html).
