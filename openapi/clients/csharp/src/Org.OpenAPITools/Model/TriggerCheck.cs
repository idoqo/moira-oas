/* 
 * Moira Alert
 *
 * This is an API description for [Moira Alert project](https://moira.readthedocs.io/en/latest/overview.html). Please check <https://github.com/moira-alert/>
 *
 * The version of the OpenAPI document: 2.5.1.48
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// TriggerCheck
    /// </summary>
    [DataContract]
    public partial class TriggerCheck :  IEquatable<TriggerCheck>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="TriggerCheck" /> class.
        /// </summary>
        /// <param name="metrics">metrics.</param>
        /// <param name="score">score.</param>
        /// <param name="state">state.</param>
        /// <param name="maintenance">maintenance.</param>
        /// <param name="maintenanceInfo">maintenanceInfo.</param>
        /// <param name="timestamp">timestamp.</param>
        /// <param name="eventTimestamp">eventTimestamp.</param>
        /// <param name="lastSuccessfulCheckTimestamp">lastSuccessfulCheckTimestamp.</param>
        /// <param name="suppressed">suppressed.</param>
        /// <param name="suppressedState">suppressedState.</param>
        /// <param name="msg">msg.</param>
        /// <param name="triggerId">triggerId.</param>
        public TriggerCheck(MetricState metrics = default(MetricState), int score = default(int), string state = default(string), int maintenance = default(int), MaintenanceInfo maintenanceInfo = default(MaintenanceInfo), int timestamp = default(int), int eventTimestamp = default(int), int lastSuccessfulCheckTimestamp = default(int), bool suppressed = default(bool), string suppressedState = default(string), string msg = default(string), string triggerId = default(string))
        {
            this.Metrics = metrics;
            this.Score = score;
            this.State = state;
            this.Maintenance = maintenance;
            this.MaintenanceInfo = maintenanceInfo;
            this.Timestamp = timestamp;
            this.EventTimestamp = eventTimestamp;
            this.LastSuccessfulCheckTimestamp = lastSuccessfulCheckTimestamp;
            this.Suppressed = suppressed;
            this.SuppressedState = suppressedState;
            this.Msg = msg;
            this.TriggerId = triggerId;
        }
        
        /// <summary>
        /// Gets or Sets Metrics
        /// </summary>
        [DataMember(Name="metrics", EmitDefaultValue=false)]
        public MetricState Metrics { get; set; }

        /// <summary>
        /// Gets or Sets Score
        /// </summary>
        [DataMember(Name="score", EmitDefaultValue=false)]
        public int Score { get; set; }

        /// <summary>
        /// Gets or Sets State
        /// </summary>
        [DataMember(Name="state", EmitDefaultValue=false)]
        public string State { get; set; }

        /// <summary>
        /// Gets or Sets Maintenance
        /// </summary>
        [DataMember(Name="maintenance", EmitDefaultValue=false)]
        public int Maintenance { get; set; }

        /// <summary>
        /// Gets or Sets MaintenanceInfo
        /// </summary>
        [DataMember(Name="maintenance_info", EmitDefaultValue=false)]
        public MaintenanceInfo MaintenanceInfo { get; set; }

        /// <summary>
        /// Gets or Sets Timestamp
        /// </summary>
        [DataMember(Name="timestamp", EmitDefaultValue=false)]
        public int Timestamp { get; set; }

        /// <summary>
        /// Gets or Sets EventTimestamp
        /// </summary>
        [DataMember(Name="event_timestamp", EmitDefaultValue=false)]
        public int EventTimestamp { get; set; }

        /// <summary>
        /// Gets or Sets LastSuccessfulCheckTimestamp
        /// </summary>
        [DataMember(Name="last_successful_check_timestamp", EmitDefaultValue=false)]
        public int LastSuccessfulCheckTimestamp { get; set; }

        /// <summary>
        /// Gets or Sets Suppressed
        /// </summary>
        [DataMember(Name="suppressed", EmitDefaultValue=false)]
        public bool Suppressed { get; set; }

        /// <summary>
        /// Gets or Sets SuppressedState
        /// </summary>
        [DataMember(Name="suppressed_state", EmitDefaultValue=false)]
        public string SuppressedState { get; set; }

        /// <summary>
        /// Gets or Sets Msg
        /// </summary>
        [DataMember(Name="msg", EmitDefaultValue=false)]
        public string Msg { get; set; }

        /// <summary>
        /// Gets or Sets TriggerId
        /// </summary>
        [DataMember(Name="trigger_id", EmitDefaultValue=false)]
        public string TriggerId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class TriggerCheck {\n");
            sb.Append("  Metrics: ").Append(Metrics).Append("\n");
            sb.Append("  Score: ").Append(Score).Append("\n");
            sb.Append("  State: ").Append(State).Append("\n");
            sb.Append("  Maintenance: ").Append(Maintenance).Append("\n");
            sb.Append("  MaintenanceInfo: ").Append(MaintenanceInfo).Append("\n");
            sb.Append("  Timestamp: ").Append(Timestamp).Append("\n");
            sb.Append("  EventTimestamp: ").Append(EventTimestamp).Append("\n");
            sb.Append("  LastSuccessfulCheckTimestamp: ").Append(LastSuccessfulCheckTimestamp).Append("\n");
            sb.Append("  Suppressed: ").Append(Suppressed).Append("\n");
            sb.Append("  SuppressedState: ").Append(SuppressedState).Append("\n");
            sb.Append("  Msg: ").Append(Msg).Append("\n");
            sb.Append("  TriggerId: ").Append(TriggerId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as TriggerCheck);
        }

        /// <summary>
        /// Returns true if TriggerCheck instances are equal
        /// </summary>
        /// <param name="input">Instance of TriggerCheck to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(TriggerCheck input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Metrics == input.Metrics ||
                    (this.Metrics != null &&
                    this.Metrics.Equals(input.Metrics))
                ) && 
                (
                    this.Score == input.Score ||
                    (this.Score != null &&
                    this.Score.Equals(input.Score))
                ) && 
                (
                    this.State == input.State ||
                    (this.State != null &&
                    this.State.Equals(input.State))
                ) && 
                (
                    this.Maintenance == input.Maintenance ||
                    (this.Maintenance != null &&
                    this.Maintenance.Equals(input.Maintenance))
                ) && 
                (
                    this.MaintenanceInfo == input.MaintenanceInfo ||
                    (this.MaintenanceInfo != null &&
                    this.MaintenanceInfo.Equals(input.MaintenanceInfo))
                ) && 
                (
                    this.Timestamp == input.Timestamp ||
                    (this.Timestamp != null &&
                    this.Timestamp.Equals(input.Timestamp))
                ) && 
                (
                    this.EventTimestamp == input.EventTimestamp ||
                    (this.EventTimestamp != null &&
                    this.EventTimestamp.Equals(input.EventTimestamp))
                ) && 
                (
                    this.LastSuccessfulCheckTimestamp == input.LastSuccessfulCheckTimestamp ||
                    (this.LastSuccessfulCheckTimestamp != null &&
                    this.LastSuccessfulCheckTimestamp.Equals(input.LastSuccessfulCheckTimestamp))
                ) && 
                (
                    this.Suppressed == input.Suppressed ||
                    (this.Suppressed != null &&
                    this.Suppressed.Equals(input.Suppressed))
                ) && 
                (
                    this.SuppressedState == input.SuppressedState ||
                    (this.SuppressedState != null &&
                    this.SuppressedState.Equals(input.SuppressedState))
                ) && 
                (
                    this.Msg == input.Msg ||
                    (this.Msg != null &&
                    this.Msg.Equals(input.Msg))
                ) && 
                (
                    this.TriggerId == input.TriggerId ||
                    (this.TriggerId != null &&
                    this.TriggerId.Equals(input.TriggerId))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Metrics != null)
                    hashCode = hashCode * 59 + this.Metrics.GetHashCode();
                if (this.Score != null)
                    hashCode = hashCode * 59 + this.Score.GetHashCode();
                if (this.State != null)
                    hashCode = hashCode * 59 + this.State.GetHashCode();
                if (this.Maintenance != null)
                    hashCode = hashCode * 59 + this.Maintenance.GetHashCode();
                if (this.MaintenanceInfo != null)
                    hashCode = hashCode * 59 + this.MaintenanceInfo.GetHashCode();
                if (this.Timestamp != null)
                    hashCode = hashCode * 59 + this.Timestamp.GetHashCode();
                if (this.EventTimestamp != null)
                    hashCode = hashCode * 59 + this.EventTimestamp.GetHashCode();
                if (this.LastSuccessfulCheckTimestamp != null)
                    hashCode = hashCode * 59 + this.LastSuccessfulCheckTimestamp.GetHashCode();
                if (this.Suppressed != null)
                    hashCode = hashCode * 59 + this.Suppressed.GetHashCode();
                if (this.SuppressedState != null)
                    hashCode = hashCode * 59 + this.SuppressedState.GetHashCode();
                if (this.Msg != null)
                    hashCode = hashCode * 59 + this.Msg.GetHashCode();
                if (this.TriggerId != null)
                    hashCode = hashCode * 59 + this.TriggerId.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
